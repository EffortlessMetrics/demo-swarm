"""Exercise the production checker, its CLI, and the actual checked-in workflow."""

from contextlib import redirect_stderr, redirect_stdout
from copy import deepcopy
import importlib.util
import io
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "scripts" / "check_pack_workflow.py"
spec = importlib.util.spec_from_file_location("check_pack_workflow", SCRIPT)
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


class PackWorkflowTests(unittest.TestCase):
    def setUp(self):
        self.text = checker.DEFAULT_WORKFLOW.read_text(encoding="utf-8")
        self.workflow = checker.parse_workflow(self.text)

    def rejected(self, workflow, expected):
        errors = checker.policy_errors(workflow)
        self.assertTrue(any(expected in error for error in errors), errors)

    def test_actual_workflow_and_default_cli_pass_without_writing(self):
        before = checker.DEFAULT_WORKFLOW.read_bytes()
        self.assertEqual(checker.policy_errors(self.workflow), [])
        with redirect_stdout(io.StringIO()) as output:
            self.assertEqual(checker.main([]), 0)
        self.assertIn("declared permissions", output.getvalue())
        self.assertEqual(checker.DEFAULT_WORKFLOW.read_bytes(), before)

    def test_rejects_missing_extra_or_nonliteral_workflow_permissions(self):
        for value in (None, {}, "read-all", "write-all", {"contents": "write"},
                      {"contents": "read", "checks": "write"},
                      {"contents": "${{ inputs.permission }}"}):
            with self.subTest(value=value):
                changed = deepcopy(self.workflow)
                changed["permissions"] = value
                self.rejected(changed, "workflow permissions")
        del self.workflow["permissions"]
        self.rejected(self.workflow, "workflow permissions")

    def test_job_overrides_cannot_widen_authority(self):
        for name in self.workflow["jobs"]:
            for value in ("write-all", "read-all", {"checks": "write"},
                          {"contents": "write"}, {"contents": ["read"]}):
                with self.subTest(job=name, value=value):
                    changed = deepcopy(self.workflow)
                    changed["jobs"][name]["permissions"] = value
                    self.rejected(changed, f"jobs.{name}.permissions")

    def test_narrow_job_override_and_extra_safe_job_are_accepted(self):
        for value in ({}, {"contents": "none"}, {"contents": "read"}):
            with self.subTest(value=value):
                changed = deepcopy(self.workflow)
                changed["jobs"]["lint"]["permissions"] = value
                changed["jobs"]["extra-safe-proof"] = deepcopy(changed["jobs"]["lint"])
                self.assertEqual(checker.policy_errors(changed), [])

    def test_every_checkout_rejects_missing_true_or_dynamic_persistence(self):
        count = 0
        for name, job in self.workflow["jobs"].items():
            for index, step in enumerate(job["steps"]):
                if step.get("uses", "").startswith("actions/checkout@"):
                    count += 1
                    for value in (None, {}, {"persist-credentials": "true"},
                                  {"persist-credentials": "${{ inputs.persist }}"}):
                        with self.subTest(job=name, value=value):
                            changed = deepcopy(self.workflow)
                            changed["jobs"][name]["steps"][index]["with"] = value
                            self.rejected(changed, "persist-credentials: false")
        self.assertGreater(count, 0)

    def test_later_and_mixed_case_checkouts_are_checked(self):
        self.workflow["jobs"]["lint"]["steps"].append({
            "uses": "Actions/Checkout@v4", "with": {"persist-credentials": "true"},
        })
        self.rejected(self.workflow, "persist-credentials: false")

    def test_separate_checkout_credentials_are_rejected(self):
        for key in ("token", "ssh-key"):
            with self.subTest(key=key):
                changed = deepcopy(self.workflow)
                changed["jobs"]["lint"]["steps"][0]["with"][key] = "${{ secrets.OTHER }}"
                self.rejected(changed, "separate checkout credentials")

    def test_empty_or_uninspectable_jobs_do_not_pass(self):
        for jobs in ({}, [], {"bad": None}, {"bad": {"steps": []}},
                     {"bad": {"uses": "org/repo/.github/workflows/proof.yml@main"}},
                     {"bad": {"steps": [{"run": "echo ok"}]}},
                     {"bad": {"steps": [None]}}):
            with self.subTest(jobs=jobs):
                changed = deepcopy(self.workflow)
                changed["jobs"] = jobs
                self.assertTrue(checker.policy_errors(changed))
        self.assertTrue(checker.policy_errors(None))

    def test_duplicate_merge_and_alias_keys_are_not_silently_normalized(self):
        cases = (
            "permissions: {contents: write}\npermissions: {contents: read}\n",
            "permissions: {contents: write, contents: read}\n",
            "jobs: {lint: {steps: [], steps: []}}\n",
            "defaults: &d {contents: read}\npermissions: *d\n",
            "permissions: {<<: {contents: write}, contents: read}\n",
        )
        for source in cases:
            with self.subTest(source=source), self.assertRaises(ValueError):
                checker.parse_workflow(source)
        self.assertIn("on", self.workflow)
        self.assertNotIn(True, self.workflow)

    def test_cli_preserves_failure_distinctions_and_source_bytes(self):
        cases = ((self.text.replace("contents: read", "contents: write", 1), 1),
                 ("permissions: [\n", 2), ("permissions: x\npermissions: y\n", 2))
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "pack.yml"
            for text, expected in cases:
                with self.subTest(expected=expected):
                    path.write_text(text, encoding="utf-8")
                    before = path.read_bytes()
                    with redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
                        self.assertEqual(checker.main(["--workflow", str(path)]), expected)
                    self.assertEqual(path.read_bytes(), before)
            with redirect_stderr(io.StringIO()):
                self.assertEqual(checker.main(["--workflow", str(path.with_name("missing.yml"))]), 2)

    def test_production_checker_and_its_tests_are_invoked_in_existing_lint_job(self):
        steps = self.workflow["jobs"]["lint"]["steps"]
        commands = [step.get("run") for step in steps]
        required = (
            "python -m pip install -r scripts/requirements-ci.txt",
            "python scripts/check_pack_workflow.py",
            "python -m unittest discover -s scripts/tests -p 'test_*.py' -v",
        )
        for command in required:
            self.assertIn(command, commands)
            step = steps[commands.index(command)]
            self.assertNotIn("if", step)
            self.assertNotIn("continue-on-error", step)
        self.assertLess(commands.index(required[0]), commands.index(required[1]))
        self.assertLess(commands.index(required[0]), commands.index(required[2]))
        self.assertEqual((ROOT / "scripts/requirements-ci.txt").read_text().splitlines()[-1],
                         "PyYAML==6.0.3")


if __name__ == "__main__":
    unittest.main()

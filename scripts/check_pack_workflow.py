#!/usr/bin/env python3
"""Check Pack CI's declared token and checkout policy without modifying files.

This is a source regression check, not proof of runtime isolation or a complete
GitHub Actions schema validator. Install scripts/requirements-ci.txt first.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import sys
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_WORKFLOW = ROOT / ".github" / "workflows" / "pack.yml"


class UniqueLoader(yaml.BaseLoader):
    """Keep scalars literal (including `on`), refusing ambiguous mappings."""

    def construct_mapping(self, node: yaml.MappingNode, deep: bool = False) -> dict:
        result = {}
        for key_node, value_node in node.value:
            if not isinstance(key_node, yaml.ScalarNode):
                raise ValueError("workflow mapping keys must be scalar")
            key = self.construct_object(key_node, deep=deep)
            if key == "<<" or key in result:
                raise ValueError(
                    f"duplicate or merged key {key!r} at line {key_node.start_mark.line + 1}"
                )
            result[key] = self.construct_object(value_node, deep=deep)
        return result


def parse_workflow(text: str) -> Any:
    # Explicitly unsupported, rather than guessing effective merged/recursive data.
    if any(isinstance(token, yaml.AliasToken) for token in yaml.scan(text)):
        raise ValueError("workflow aliases are unsupported by this bounded checker")
    return yaml.load(text, Loader=UniqueLoader)


def policy_errors(workflow: Any) -> list[str]:
    if not isinstance(workflow, dict):
        return ["workflow must be a mapping"]
    errors = []
    if workflow.get("permissions") != {"contents": "read"}:
        errors.append("workflow permissions must be exactly contents: read")
    jobs = workflow.get("jobs")
    if not isinstance(jobs, dict) or not jobs:
        return errors + ["workflow must contain nonempty jobs"]
    for name, job in jobs.items():
        where = f"jobs.{name}"
        if not isinstance(job, dict):
            errors.append(f"{where} must be a mapping")
            continue
        if "permissions" in job:
            permissions = job["permissions"]
            if not isinstance(permissions, dict) or any(
                key != "contents" or value not in ("read", "none")
                for key, value in permissions.items()
            ):
                errors.append(f"{where}.permissions widens or obscures contents-only access")
        steps = job.get("steps")
        if "uses" in job or not isinstance(steps, list) or not steps:
            errors.append(f"{where} needs explicit steps; reusable jobs require separate review")
            continue
        checkouts = 0
        for index, step in enumerate(steps):
            at = f"{where}.steps[{index}]"
            if not isinstance(step, dict):
                errors.append(f"{at} must be a mapping")
                continue
            action = step.get("uses", "")
            if not isinstance(action, str):
                errors.append(f"{at}.uses must be a literal action reference")
                continue
            if action.casefold().startswith("actions/checkout@"):
                checkouts += 1
                inputs = step.get("with")
                if not isinstance(inputs, dict) or inputs.get("persist-credentials") != "false":
                    errors.append(f"{at} must set persist-credentials: false")
                if isinstance(inputs, dict) and any(key in inputs for key in ("token", "ssh-key")):
                    errors.append(f"{at} must not supply separate checkout credentials")
        if not checkouts:
            errors.append(f"{where} has no inspectable actions/checkout step")
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workflow", type=Path, default=DEFAULT_WORKFLOW)
    args = parser.parse_args(argv)
    try:
        text = args.workflow.read_text(encoding="utf-8-sig")
        errors = policy_errors(parse_workflow(text))
    except (OSError, UnicodeError, ValueError, yaml.YAMLError) as error:
        print(f"Pack workflow could not be checked: {error}", file=sys.stderr)
        return 2
    if errors:
        for error in errors:
            print(f"Pack workflow policy: {error}", file=sys.stderr)
        return 1
    print("Pack workflow policy passed (declared permissions and checkout inputs only).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

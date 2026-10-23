---
name: test-runner
description: Run the relevant tests for the current change and summarize results. Use in Flow 3 (Build) and optionally in Flow 5 (Gate).
allowed-tools: Bash, Read, Write
---

# Test Runner Skill

You are a helper for running tests in this repository.

Execute the admitted test selection and capture output. Test quality and proof
selection belong to the caller; do not silently widen or weaken that selection.
In source-only review mode, do not execute candidate-controlled commands. Return
the requested experiment to the admitted writer/proof worker.

---

## Purpose

Capture raw output, exit codes and structured counts for the selected invocation.

**What this skill does NOT do:**

- Write or modify tests (that's test-author)
- Judge test quality (that's test-critic)
- Make decisions about what to test (that's orchestrator / test-strategist)
- Classify failures (that's flakiness-detector)

---

## When to Use

| Context                        | Selection Strategy       | Example                            |
| ------------------------------ | ------------------------ | ---------------------------------- |
| **AC loop (Flow 3)** | Relevant AC proof | Actual test IDs/files and useful failure policy |
| **Post-AC verification** | Affected behavior/dependencies | Reassess proof after a material change |
| **Hardening / qualification** | Admitted applicable obligations | Include expensive tests when their condition selects them |
| **Quick sanity check** | Explicit smoke selection | Small observation; not a full qualification claim |

Read the caller's selection, the existing test plan and native policy. Conditional
or expensive proof records its obligation/witness, applicability scenario,
selector and actual consumer, phase, cost/deadline/resources and evidence-reuse
limits. Tags are selectors only when a runner consumes them. Missing scope or an
unsupported filter is a selection gap, not permission to run everything.

Reuse applicable original evidence where authorized; a new reviewer is not itself
a reason to replay it. When required proof applies, execute it, reuse admissible
evidence, or report it unproven. Budget expiry, zero matches and unavailable tools
cannot satisfy that obligation. Keep expensive proof when it is the cheapest
valid method; record and admit its actual cost. Local development execution does
not request CI. On the selected queue route, CI qualifies the actual composition.

---

## Test Selection Strategies

### 1. Run All Tests (Full Suite)

Use only when the admitted portfolio requires it or it is the cheapest valid
method for the current obligation. Record that reason, cost and deadline. A flow
name or missing scope does not select a full suite.

```bash
# Rust
cargo test --workspace --tests --color=always

# Python (pytest)
pytest --color=yes -v

# JavaScript (jest)
npm test -- --colors

# Go
go test ./...
```

### 2. Run Changed Tests (Scoped by Diff)

Use when: Focused verification of what changed since main.

```bash
# Get changed files
git diff --name-only origin/main...HEAD

# Filter to test files and run those specifically
# (Framework-specific filtering)
```

### 3. Run Related Tests (Dependency Aware)

Use when: Implementation changed, need to run tests that exercise that code.

For Rust:

```bash
cargo test -p <crate> -- <test-name-pattern>
cargo test --test <integration-test-name>
```

For pytest:

```bash
pytest tests/unit/test_<module>.py -v
pytest -k "auth or login"
```

### 4. Run AC-Scoped Tests

Use when: Verifying a specific Acceptance Criterion in the AC loop.

Test naming conventions for AC filtering:

- `test_ac_001_*` (name prefix)
- `@AC-001` marker/tag
- File-based: `tests/ac_001_*.py`

```bash
# pytest with marker
pytest -m "AC_001" --color=yes

# cargo test with pattern
cargo test ac_001

# jest with pattern
npm test -- --testNamePattern="AC-001"
```

### 5. Run Smoke Tests Only

Use when: Quick sanity check, not full verification.

```bash
# If smoke marker exists
pytest -m smoke --color=yes

# Use an existing explicit test selection when no smoke marker exists.
# A failure limit such as -x does not select the first N tests or a smoke suite.
```

---

## Commands by Framework

### Rust (cargo test)

```bash
# Full suite
cargo test --workspace --tests --color=always

# Specific crate
cargo test -p <crate-name>

# Pattern match
cargo test <pattern>

# Single test
cargo test <full::path::to::test>

# Integration test file
cargo test --test <name>

# Serial execution, only when isolation requires it; this is not fail-fast
cargo test <pattern> -- --test-threads=1
```

Cargo stops after a failing test executable by default; tests within that
executable run to completion. `--no-fail-fast` changes the executable-level
policy. `--test-threads` controls concurrency. Do not substitute serialization
for fail-fast or add unstable flags to a stable toolchain. See the
[Cargo test contract](https://doc.rust-lang.org/cargo/commands/cargo-test.html)
and [libtest options](https://doc.rust-lang.org/rustc/tests/index.html).

### Python (pytest)

```bash
# Full suite
pytest --color=yes -v

# Specific file
pytest tests/unit/test_auth.py -v

# Pattern match
pytest -k "login or session" -v

# Marker-based
pytest -m "unit" -v
pytest -m "AC_001" -v

# Fail-fast
pytest -x --color=yes

# With coverage
pytest --cov=src --cov-report=term-missing
```

### JavaScript/TypeScript (jest)

```bash
# Full suite
npm test -- --colors

# Specific file
npm test -- --colors tests/auth.test.ts

# Pattern match
npm test -- --testNamePattern="login"

# Fail-fast
npm test -- --bail --colors

# With coverage
npm test -- --coverage
```

### Go (go test)

```bash
# Full suite
go test ./...

# Specific package
go test ./pkg/auth/...

# Pattern match
go test -run "TestLogin" ./...

# Fail-fast
go test -failfast ./...

# Verbose
go test -v ./...
```

---

## Output Format

### Raw Output

Use the existing `test_output.log` working path. Before overwriting a result that
is cited or needed for reuse, retain the original in the repository's existing
run/artifact storage. Cite its source, command/environment, selected/executed
tests, outcome and applicability; a later summary is not a new execution.

### Structured Summary

Save parsed summary to `test_summary.md` with this structure:

`Result: PASS | FAIL` describes an observed command outcome, not satisfaction of
the proof portfolio. Record unproven obligations in Notes using `UNVERIFIED` and
their next action. For no execution (including source-only mode or unavailable
tooling), omit the command-result line, use null exit code/counts and explain
the limitation; do not fabricate PASS/FAIL or extend serialized status enums.

```markdown
# Test Summary

## Overall Status

- **Result:** PASS | FAIL
- **Exit Code:** <int|null>
- **Duration:** <time>

## Counts

- Passed: <int>
- Failed: <int>
- Skipped: <int>
- xfailed: <int>
- xpassed: <int>

## Failing Tests (if any)

- `path::to::test_name` - <short error>
- `path::to::other_test` - <short error>

## Notes

- <applicable obligation dispositions; missing required proof remains UNVERIFIED; next action>

## Top Error Snippets
```

<first 5-10 lines of first failure>

```

```

### Canonical Summary Line

For machine parsing, include a canonical line:

```
passed=15 failed=2 skipped=1 xfailed=0 xpassed=0
```

Use `null` for any count that cannot be reliably extracted.

---

## Handling Test Failures

### Exit Codes

| Code | Meaning                   |
| ---- | ------------------------- |
| 0    | Command succeeded; inspect selected/executed tests before claiming proof |
| 1+   | Non-success; distinguish test, build, instrument or environment failure |
| null | Command could not execute |

### Failure Output

When tests fail:

1. Capture the full output to `test_output.log`
2. Extract failing test names to `test_summary.md`
3. Include up to 20 lines of the most relevant error output
4. Report exit code accurately

### Do Not Modify on Failure

The test-runner skill does not fix failing tests. It reports results. Routing decisions belong to the orchestrator. Fixes belong to code-implementer or test-author.

---

## Flaky Test Awareness

The test-runner itself does not classify flakiness. However, it should:

1. **Record raw results faithfully** - Each run produces accurate counts
2. **Include test identifiers** - So flakiness-detector can compare across runs
3. **Note any timeout or intermittent signals** - In the summary notes

For actual flakiness classification, the orchestrator routes to `flakiness-detector`, which:

- Re-runs failures with a budget
- Classifies: DETERMINISTIC_REGRESSION vs FLAKY vs ENV_TOOLING
- Produces a worklist for routing

---

## Integration with Agents

### Called by: test-executor

The `test-executor` agent invokes this skill and writes the formal artifact:

- `.runs/<run-id>/build/test_execution.md`

The test-executor handles:

- Mode selection (verify vs verify_ac)
- Fail-fast decisions based on flow context
- Formal handoff to orchestrator

### Called by: test-author

The `test-author` agent may invoke this skill to verify tests work:

- Quick run of newly written tests
- Scope to just the tests being authored
- Not a formal execution report

### Informs: flakiness-detector

The `flakiness-detector` reads test-runner output to understand what failed, then re-runs to classify. It does not call test-runner directly; it runs tests itself with a rerun budget.

---

## Configuration

### Repository Config

If `demo-swarm.config.json` exists, read test commands from:

```json
{
  "commands": {
    "test": "cargo test --workspace --tests --color=always",
    "test_scoped": "cargo test -p {crate}",
    "test_ac": "cargo test {ac_pattern}"
  },
  "flakiness": {
    "budget_seconds": 180,
    "rerun_count": 3,
    "command": null
  }
}
```

### Fallback Detection

If no config exists, detect the stack:

- `Cargo.toml` present → Rust/cargo test
- `package.json` with test script → npm test
- `pytest.ini` or `pyproject.toml` → pytest
- `go.mod` present → go test

Do not invent commands. If detection fails, record `missing_required` and bounce to `pack-customizer`.

---

## Examples

### Example 1: AC-Scoped Run (Flow 3 Microloop)

```bash
# Run matching AC-001 tests; Cargo's failure policy is per executable
cargo test ac_001
```

Record actual counts, exit code, duration and failing test IDs in
`test_summary.md`. Confirm the intended tests matched; do not infer coverage
from the AC filter's name.

### Example 2: Explicitly Selected Full Suite

```bash
cargo test --workspace --tests --color=always
```

For example, exit code 0 with 127 passed, 3 skipped and 2 xfailed is command
success. Record those actual counts. The selected proof remains `UNVERIFIED`
until applicable required obligations for the skipped/xfail cases are resolved;
an unavailable service or known-issue link alone does not waive them.

### Example 3: Changed Files Scope

```bash
# Identify changed files
git diff --name-only origin/main...HEAD | grep '\.rs$'

# Run tests for changed crates
cargo test -p auth_service -p session_manager
```

---

## Troubleshooting

### Test Command Not Found

**Symptom:** `cargo: command not found` or similar.

**Solution:** This is an environment issue. Record as ENV_TOOLING and bounce to fix environment. Do not continue with broken tooling.

### Cannot Determine Counts

**Symptom:** Test output does not match expected format.

**Solution:** Record counts as `null` rather than guessing. Note the parsing issue in summary. The skill contract is to report accurately, not to fabricate.

### Tests Hang or Timeout

**Symptom:** Tests do not complete within reasonable time.

**Solution:** Note the timeout in summary. If the run was partial, include whatever counts were observed. Record as potentially flaky for flakiness-detector to investigate.

### No Test Files Found

**Symptom:** Test command runs but finds nothing to test.

**Solution:** Report the actual zero counts. If the selection was meant to
establish an obligation, zero matching tests leave it unproven. If nothing was
applicable, cite that separate decision; do not report a test pass for it.

---

## Behavior (Inherited from Original)

1. Prefer scoped test runs:
   - Use `git diff --name-only origin/main...HEAD` to list changed files when available.
   - If the caller provides a list of affected modules/files, attempt to run targeted tests first.

2. Runtime flags and run bounds:
   - Prefer to keep runs bounded; if the full suite is required, note this in the summary.

3. Capture output and artifacts:
   - Use `test_output.log` and `test_summary.md`, preserving cited original executions before replacing those working paths.
   - `test_summary.md` distinguishes observed command outcome from obligation disposition, with actual failing test names, error snippets and counts.

4. Failure handling:
   - Exit status is used by calling subagent; include failing test names in `test_summary.md`.

5. Do not modify source or tests.

6. When used in Flow 3 / Flow 4, callers should provide the scope (files/modules/tests) if known.

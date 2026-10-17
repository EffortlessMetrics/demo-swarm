# DemoSwarm

A reusable SDLC pack for Claude Code: investigate a problem, build and challenge
a coherent candidate, carry executed evidence into review, qualify deliberately,
and make a separate integration decision.

The goal is useful software with less rework and operator effort. Faster code
generation alone does not establish quality; neither do green panels or receipts
without meaningful tests and current source.

## Start

```text
/customize-pack
/flow-1-signal "Add a health check endpoint"
```

Continue through the relevant flows, or enter an existing issue/PR at its first
missing or stale judgment. Read [CLAUDE.md](CLAUDE.md) for the operating contract
and [late qualification](docs/reference/late-qualification.md) for migration
status. The installed consumer's workflow and protection remain authoritative;
this instruction update does not silently change their triggers.

## The flows

| Entry | Outcome |
|---|---|
| Signal | Investigated problem, intended behavior and falsifiers |
| Plan | Challenged design and bounded acceptance/rollback claim |
| Build | One coherent candidate, focused proof and quality improvements |
| Review | Substantive findings, verified repairs and current dispositions |
| Gate | Explicit independent qualification and its actual result |
| Deploy | Fresh final judgment, protected merge and landed reconciliation |
| Wisdom | Evidence-backed product and operating-method improvement |

These are recurring questions and useful entrypoints, not a mandatory sequence
of fresh agents. Keep useful writer and build context warm. Different readers,
tools and oracles can challenge the same candidate concurrently.

A Draft exposes source and evidence. Draft/Ready is not a qualification request.
Source review can complete while independent CI is still NotRun. An explicit
request binds the candidate, reviewed evidence and selected obligations; an old
label cannot authorize a successor. Qualification does not merge or release.
The historical Deploy command name remains for compatibility, but merge, tag,
public release and production deployment are different authorized operations.

## Review surface

The PR description should help a reviewer locate the claim, actual source,
executed proof, material findings, limitations and next action. It is not a
substitute for inspecting load-bearing code, real consumers and plausible wrong
behavior. A clean first review does not suppress later substantive investigation.

Git owns versioned source and decisions. GitHub owns current issue/PR/review/check
and merge facts. `.runs/<run-id>/` retains useful local evidence and helper
compatibility; it is not a second live-state authority. Summaries do not multiply
the number of independent observations.

[Flow Studio](https://github.com/EffortlessMetrics/flow-studio-swarm) is the related
flow visualization/harness project. Its implementation and distribution roles
remain separate; updating this pack does not activate or release that system.

## Layout and validation

| Location | Content |
|---|---|
| `.claude/commands/` | Flow entrypoints |
| `.claude/agents/` | Optional focused workers and reviewers |
| `.claude/skills/` | Native helpers and task procedures |
| `.claude/rules/` | Loaded operating guidance |
| `docs/` | References, teaching material and historical rationale |

```bash
bash .claude/scripts/pack-check.sh --no-color
```

Use the actual repository's validation requirements. Instruction/source checks,
harness behavior, downstream adoption and installed-product proof are different
acceptances. Issue #22 retains the unfinished historical-guide, helper and
multi-harness migration; no complete downstream CI cutover is claimed here.

Created by Steven Zimmerman (@EffortlessSteven). Licensed under Apache-2.0.

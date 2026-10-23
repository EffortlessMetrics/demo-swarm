# DemoSwarm operating contract

This pack supplies focused engineering procedures, native helpers and retained
evidence. The accountable root owns the integrated result. Work starts from the
selected issue or existing candidate, not from a required roster of agents.

## Current authority and migration

For the development lifecycle, this file, `.claude/rules/00-doctrine.md`,
`.claude/rules/60-flow-orchestrators.md` and the current Build/Review/Gate/Deploy
commands supersede older instructions to wake CI through Draft/Ready, repeat a
fixed agent checklist, or interpret a gate verdict as release authorization.
Other rules and specialist guidance still apply within those boundaries.
See [the migration reference](docs/reference/late-qualification.md) for what is
implemented and what still needs consumer qualification under issue #22.

Accepted product direction governs the intended result; source and evidence
govern claims. An instruction migration is not an Actions/settings migration.
Inspect the consuming repository's installed workflow, required checks and
actual request operation. Preserve those controls until its replacement is
qualified. Never invent a request command or grant yourself bypass authority.

## Selected integration mode

The October 21 RIPR/Perl ruling selects native queue-time qualification. Follow
[native queue-time qualification](docs/reference/native-queue-qualification.md)
for its target, safe cutover, rollback and acceptance cases. Selection is not
activation and does not opt every pack consumer into a queue.

The October 22 clarification requires no CI workflow on Draft, Ready or ordinary
publication/update events in the selected steady state. Run useful focused tests
and substantive review locally before enqueue. Required PR admission context
publication is a separate explicit admission operation, not permission to retain
a cheap PR-triggered workflow. Its producer and native enforcement must be
qualified; missing admission is not success.

Where older rules, helpers or explanation docs forbid queues universally or put
all final judgment after qualification, this mode-specific contract governs:
keep the installed legacy route until the consumer verifies its replacement;
on the verified queue route, complete product/scope/merge authorization before
enqueue, qualify the actual group, and reconcile native landing afterward.
Enqueue is conditional authorization to land, not a neutral test request. Do not
use generic auto-merge to bypass the legacy final decision. Release authority,
existing helper schemas and all unaffected review/evidence controls stay separate.

## Entry and ownership

Continue actionable work on the owned PR before creating a duplicate. Resolve a
controlling issue, inspect the premise, current source, consumers, dependencies,
existing findings and relevant decisions. Define one coherent acceptance and
rollback claim. An old issue checkbox or local run summary is not live state.

Keep one integration owner and one writer for contested candidate surfaces.
Read-only investigation and review need no reservation. Delegate when another
context, tool, oracle or perspective changes what we can discover. The root may
perform bounded work directly and must reconcile delegated results. A role name
does not establish independence or prohibit useful work.

Return to the earliest question invalidated by new evidence. Do not restart the
whole process after an unrelated SHA change. Do not treat an unchanged SHA as
proof that no material review finding has arrived.

## Public entrypoints

| Command | Useful outcome |
|---|---|
| `/customize-pack` | Adapt real commands and supported repository surfaces |
| `/flow-1-signal` | Investigated problem, intended behavior and falsifiers |
| `/flow-2-plan` | Challenged design and bounded implementation claim |
| `/flow-3-build` | Coherent implementation, discriminating warm proof and quality work |
| `/flow-4-review` | Current substantive findings and evidence-backed repair dispositions |
| `/flow-5-gate` | Applicable qualification; queue admission requires prior conditional merge authorization |
| `/flow-6-deploy` | Integration judgment before the consequential merge/enqueue action, then landed reconciliation |
| `/flow-7-wisdom` | Evidence-backed product and operating-method improvement |

Names are stable navigation. They do not require a fresh agent, every historical
artifact or a fixed sequence of calls. Flow 6's legacy name does not grant tag,
package, release, upstream-promotion or production-deployment authority.

## Reasoning and proof

Challenge premise, plan, test stimulus/oracle, production use, error paths,
compatibility, test economics, simplicity, documentation and product fit where
relevant. Keep the writer and useful build context warm while readers challenge
the candidate. A first green test is not a completed review.

For evidence retain actual source bytes or immutable identity, selected and
executed subjects, command/environment, outcome, capture limitations and an
accessible original. HEAD alone does not identify dirty or staged source. A
hash authenticates neither the producer nor the fact of execution. Preserve
historical results; separately decide present applicability.

Use existing tool shims rather than assuming installed PATH helpers:

```bash
bash .claude/scripts/pack-check.sh [OPTIONS]
bash .claude/scripts/demoswarm.sh <command>
```

The helpers' existing schemas remain unchanged. Missing/unknown counters must
not be invented. A failed helper invocation remains non-successful until its product or instrument
cause is understood; it is not an instruction to fabricate a passing receipt.

## Publication and consequential effects

Stage only intended source. Preserve unrelated staged/unstaged work. Scan the
actual publication surface for secrets and run applicable focused validation
before committing. Do not make evidence-only or empty commits to wake CI.

The selected target starts no CI on commits, ordinary pushes or Draft/Ready
transitions. Local proof and source review precede native queue qualification. Explicitly request the current
reviewed candidate through the installed adapter; retain request identity and
readback. A retained label cannot authorize a successor. A lost response needs
reconciliation, not blind retry.

On the installed legacy route, complete qualification and then make the separate
final judgment before a protected expected-head merge. On a verified native queue
route, make product/scope judgment and conditional merge authorization before
enqueue; actual G qualification and current eligibility govern native protected
landing. Do not add a second full qualification or an imaginary post-green pause.
In either mode, inspect the landed result. Tagging, publication and deployment
need their own authorization and evidence; a merge recommendation supplies neither.

## GitHub Access + Content Mode

Respect the selected repository, credential scope and publication authorization.
Sanitize content before it leaves the workspace. Existing helper fields such as
`safe_to_commit`, `safe_to_publish` and `proceed_to_github_ops` report their
specific prerequisite; no field grants every GitHub effect.

A failed source push does not forbid an authorized, sanitized blocker comment.
It does forbid claiming remote source exists. When only restricted reporting is
safe, disclose the limitation without source/secrets. Record attempted, accepted
and independently observed effects separately. Do not broaden credentials to
make a report convenient.

GitHub owns live issues, PRs, reviews, checks and merges. Git owns versioned
source and durable decisions. `.runs/<run-id>/` can preserve local evidence and
existing helper compatibility; it is not a second live work database. Avoid
tracked heartbeat/state mirrors and raw private logs. A sender-local path is not
a handoff until the receiver can obtain the required source/evidence.

## Completion and continuation

`VERIFIED` applies to the named claim and actual evidence, not universal
correctness. `PARTIAL` and `UNVERIFIED` retain progress, limitations and the next
useful action. `CANNOT_PROCEED` names the concrete instrument, access,
infrastructure or decision blocker. Keep independent eligible work moving.

Do not wait in a polling worker for an already observed remote operation. Retain
its exact identity and wake condition; do useful independent work or checkpoint.
A child return, opened PR, green panel or merged leaf does not complete a larger
goal. Separate product learning, change delivery, released/installed delivery
and method learning.

Historical explanation docs remain useful provenance, not permission to restore
superseded behavior. Consult them for context and update a stale consumer when
it affects the current claim. Do not load the whole archive at every stage.

# Warm review and late qualification: source migration

Owner: [#22](https://github.com/EffortlessMetrics/demo-swarm/issues/22).
Status: source candidate; downstream live adoption is not established.

This reference records the intended method and the boundaries a consumer must
implement. It does not select DemoSwarm as the canonical owner of every product
or replace Flow Studio, repository-local proof policy, or a native harness.

## Why these changes exist

The old pack attaches Draft publication to waking CI, separates work into a
fixed specialist roster, requires two clean passes, and treats equal HEAD and
a green panel as sufficient freshness/completion. Those shortcuts conflate
questions, evidence and transitions. They can repeat expensive work, lose warm
context or miss findings that arrive without a source change.

The replacement keeps focused reasoning while removing that accidental coupling.
Code, tests, source summaries and generated receipts are useful only insofar as
they support the real claim and user outcome. No instrument, model identity or
panel establishes universal correctness.

## Contract to carry across the existing flows

| Existing flow | Intended responsibility | Must not imply |
|---|---|---|
| Signal / Plan | Establish actual consumer, premise, scope, alternatives and falsifiers | A plan is executed proof, or every small fix needs every artifact |
| Build | One warm writer, red/green tests, recurring quality questions, useful publication | A commit or Draft PR requests qualification |
| Review | Differentiated criticism, current findings and joined repair | Two identical clean passes establish independent sufficiency |
| Gate | Explicit current-candidate qualification, mandatory plus risk-directed proof | A label, admission acknowledgement or skipped job is successful proof |
| Deploy | Fresh final product/current-repository judgment, authorized protected merge and reconciliation | Qualification green authorizes auto-merge or a release |
| Wisdom | Evidence-backed correction of the product and operating method | Well-formed documents prove agents loaded or followed them |

These are mapping responsibilities, not a mandatory stage state machine. A
question can recur; a candidate may enter midstream; another implementation can
fill the same responsibility. A narrow test-oracle fix does not invalidate an
unrelated architecture review.

## Fixed boundaries, flexible reasoning

- Ordinary commits, pushes and Draft/Ready changes do not request expensive CI.
- An explicit request binds the current candidate, review/evidence and actual
  selected execution. A retained label cannot authorize a successor.
- One normal complete CI run is <=20 minutes; queue delay is a different metric.
  Necessary new findings or classified instrument failures can justify a new
  attempt, with the cause and original evidence preserved.
- Available checks, mandatory obligations and risk-directed selections are
  different populations. Unknown applicability is not a no-op.
- Qualifying source review, proof execution, result publication, final judgment,
  protected merge and installed delivery are different states.
- No routine auto-merge, PR merge queue or every-merge full replay is part of the
  target. Ordinary main health uses both one hour and ten merges from its
  baseline; separately governed incident/deep/release work remains available.
- One candidate writer does not require reader reservations or a permanent agent
  hierarchy. Real external waits release attention, not ownership of the goal.
- Staged and dirty proof records its actual inputs. Reuse preserves original
  provenance and current applicability; hashes and exit codes alone do not
  prove producer authenticity, nonempty execution or a meaningful test oracle.

## Source and active behavior must not be confused

The first source slice updates the loaded doctrine and orchestration rules.
It does not silently edit the consumer's Actions or protection. Remaining
#22 consumers include CLAUDE, README, actual flow-3/4/5/6 commands, repo-operator,
review/test skills, quality scorecards, examples and customization/distribution.
They must be reconciled before declaring a coherent new pack release. Do not
ship these files as proof that downstream CI is already migrated.

When a consumer still has the old route, inspect and report that fact. Keep
its actual protected proof satisfiable until the replacement request, result,
cache and settings generation is qualified. Source work can proceed without
creating an artificial dependency on a new controller, tower or host fleet.

## Discriminating adoption cases

Use these as independently graded cases; giving a worker the expected answer
is instruction review, not a blind behavior test.

| Input | Required distinction |
|---|---|
| H1 is labeled merge-ready, then a repair pushes H2 | Preserve H1 evidence; no implicit H2 request |
| A test ran on dirty bytes and only old HEAD was retained | Repeat the available narrow test against captured inputs; do not invent binding |
| A test rejects the real wrong-boundary control but a static sensor stays noisy | Inspect the limitation; do not weaken the test merely to satisfy the sensor |
| Green qualification, then a material finding on the same head | Withhold merge and investigate; do not falsify the earlier test result |
| An exact request is already running | Retain run identity/wake event; no duplicate request or idle polling worker |
| A merge landed but packaged installation has not been exercised | Reconcile the merged claim; retain installed delivery as unproved |
| Method M2 is valid text but has not been loaded by harness Y | No claim of behavioral adoption on Y |

Record source/method revision, actual loaded inputs, harness/model/environment,
observed action, original evidence and remaining limitation. Compare a real
repair across different consumers before extracting more shared machinery.

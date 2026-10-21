# Native queue-time qualification

## Scope and decision

On October 21, 2026, Steven selected native GitHub merge-queue qualification for
RIPR and Perl LSP. This changes the integration mechanism, not the requirement
for cheap development, substantive review, trustworthy proof or protected landing.

This reference is an instruction-source contract. It does not establish that a
consumer has installed it. The consuming repository's observed workflows and
complete live enforcement union determine its current operating mode. Other
consumers are not automatically opted into a queue.

Use three distinct states:

- **Legacy protected route:** use the actual installed request and final merge
  procedure; do not substitute a proposed queue command.
- **Queue migration:** stage and qualify the replacement under its existing
  controller while preserving enforceable proof on the old route.
- **Verified queue route:** final product/scope/merge authorization precedes
  enqueue; passing required integration proof permits native protected landing.

RIPR's controller is [ripr-swarm#4984](https://github.com/EffortlessMetrics/ripr-swarm/issues/4984).
Perl's request and activation owners are
[perl-lsp-swarm#17900](https://github.com/EffortlessMetrics/perl-lsp-swarm/issues/17900)
and [#10065](https://github.com/EffortlessMetrics/perl-lsp-swarm/issues/10065).
Pack source and loaded-consumer acceptance remain [#22](https://github.com/EffortlessMetrics/demo-swarm/issues/22).
Do not start a competing caller, scheduler, readiness database or fleet project.

## Evidence and authorization subjects

| Subject | Meaning | What it can establish |
|---|---|---|
| H | Reviewed PR head and its source tree | Candidate review and focused proof |
| P | A PR event's synthetic base-plus-head integration | That historical composition, not an arbitrary later base |
| G | The native merge-group commit/tree and ordered constituent heads | The integration composition being considered for landing |
| M | The actual landed commit/tree | What reached the target branch |

Retain tested source, commands, toolchain/policy identities, run/attempt,
selected obligations, actual outcomes and accessible original evidence. Reused
proof keeps its original identity. H is not G; a successful control workflow on
main is not automatically proof for an input SHA. Squash commit identity may
change; compare the corresponding tested and landed tree, not commit equality.
For cumulative groups, reconcile the correct landed prefix rather than assuming
that the first landed PR has the final group's tree.

The selected queue lifecycle is:

```text
cheap mutable implementation and Draft publication
-> focused proof, substantive review, joined repairs
-> current product/scope judgment and authorization for exact H
-> enqueue through the installed native adapter
-> one applicable expensive qualification transaction on G
-> native protected landing if all required conditions remain satisfied
-> cheap M reconciliation and acceptance update
```

Enqueue is consequential: it authorizes automatic landing on successful proof.
It is not a neutral way to ask for tests. Source changes or a material adverse
finding withdraw eligibility and require affected review/proof before re-entry.
A later finding at unchanged H must still be able to stop landing. Keep the
candidate owner accountable while doing independent work instead of polling.

## GitHub constraints that determine the design

GitHub couples PR and merge-group required checks. Required contexts must be
satisfied before enqueue and must also report on G. The single-expensive-run
target therefore needs genuine cheap PR admission plus expensive G proof,
protected by enforced queue-only landing. A skipped job or unconditional success
is not admission or product proof. Preserve expected producer/application binding.

Do not change a required PR result from qualification to cheap admission while
direct landing can still consume it. Every required context needs an explicit
G disposition, including metadata checks that do not compile anything. Unknown
membership, missing results, wrong subject/app, incomplete pagination, cancelled
work or a never-executed required child remains non-successful.

Build concurrency controls speculative queue builds. Minimum/maximum merge
limits control which entries land together; they do not promise one build for a
batch. Begin the activation canary with build concurrency 1, squash and all
entries required to pass. One-entry landing simplifies attribution during the
canary. Increase concurrency only from measured pass rate, invalidation cost,
arrival rate and available runner capacity; a 35-minute serial lane can admit
only about 1.7 successful entries an hour before failures and overhead.

Target normally <=20 minutes of complete active qualification, including setup,
children and finalization. Queue wait is separate. Set a finite status timeout
from observed valid runtime; it is not permission to call a long run efficient.
Measure all PR, queue, main, failed, retried, cancelled, local and review costs.

## Safe activation and rollback

1. Inventory current source, all applicable classic/ruleset controls, required
   contexts and producer bindings, runner trust, cache writers and active runs.
   A checked-in desired configuration is not live enforcement.
2. Complete the G producer and cheap admission contracts, including exact group
   membership, actual checkout identity, late review withdrawal and all required
   contexts. Prove cold dependency preparation independently of warm cache hits.
3. Stage under non-required rehearsal identities while keeping the old required
   proof intact. Source/rehearsal evidence is not an activated native queue.
4. Qualify the existing producer on G; enable queue enforcement through the
   authorized settings owner and read it back. During the bounded bootstrap,
   preserve full PR qualification. Record that temporary duplicate cost rather
   than hiding it as the steady-state design.
5. After queue-only landing and every protected G producer are demonstrated,
   switch PR contexts to real cheap admission and retire duplicate expensive
   label/ordinary-PR/main-push routes. Sweep callable children and advisory
   consumers as well as top-level triggers; preserve distinct release/deep work.
6. Record a native enqueue, actual G execution, protected landing and matched M
   readback before claiming deployment. Observe the first operating cohort for
   false passes, false blocks, queue age, repair time and cost per accepted change.

For rollback, pause new admissions, reconcile in-flight work and restore the
full protected PR qualification path first. Verify that it works before removing
queue-only enforcement. Never create a window in which cheap admission alone
can authorize direct landing. Restore one coherent settings/producer/cache-writer
version; do not mix generations. Documentation rollback alone changes no live rule.

## Main health and repairs

A confirmed main-health incident has one accountable integration owner, not an
immortal polling thread. Parallel read-only diagnosis is useful; competing repair,
revert and dependency-repin writers are not. Pause ordinary queue admission and
route the designated repair through the same protected proof. The health guard
must permit a verified repair without allowing an arbitrary bypass or waiting
for main to repair itself. A queue cannot fix hidden fixture dependencies, flaky
tests or an incorrect test oracle.

After M, reconcile identity and the smallest useful landed behavior. Do not replay
the whole qualification merely because a push occurred. Preserve independently
admitted incident, release and deep checks and the existing separately governed
main-health cadence. A merge does not authorize publication, deployment to users,
upstream promotion or a release.

## Discriminating acceptance cases

These are required observations for the consumer rollout, not claims that this
source document executes them:

| Case | Required result |
|---|---|
| Two individually green PRs conflict semantically | Combined G fails before either incompatible composition lands |
| Old P is green after relevant main movement | It cannot substitute for current G proof |
| H changes after review or request | Old admission/review is not inherited |
| Material finding arrives at unchanged H | Eligibility is withdrawn; historical test evidence remains historical truth |
| Required metadata context has no G producer | Activation refuses instead of producing a permanently waiting queue |
| Required child is skipped, absent, wrong-app, wrong-SHA or from another attempt | Final protected result is non-successful |
| All selected jobs never start but the wrapper exits zero | No product qualification is reported |
| Warm cache hides an undeclared fixture dependency | Cold preparation exposes and repairs the dependency contract |
| Queue predecessor is removed or fails | Successor recomposition receives new identity and affected qualification |
| Duplicate request or lost response | Existing native operation is reconciled, not blindly repeated |
| Main is red and an accepted repair exists | One repair owner can qualify the repair without bypassing protection |
| G passes but M does not correspond | Landing incident; no false completed/qualified claim |
| Rollback is requested during active work | Full PR proof is restored before direct landing is possible |
| A consumer still runs the legacy route | Use that actual route; do not infer deployment from this document |

Primary platform contracts: [Managing a merge queue](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-a-merge-queue),
[merge_group events](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#merge_group),
and [ruleset merge-queue settings](https://docs.github.com/en/enterprise-cloud@latest/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets#require-merge-queue).

# Native queue-time qualification

## Scope and decision

On October 21, 2026, Steven selected native GitHub merge-queue qualification for
RIPR and Perl LSP. The October 22 clarification requires **no CI on Draft or
Ready**: useful local tests and substantive review finish before enqueue; CI
qualifies the actual merge group. Do not reinterpret this as permission for
cheap automatic PR workflows. Ordinary publication and updates start no CI in
the selected steady state.

This reference is an instruction-source contract. It does not establish that a
consumer has installed it. Observed workflows and the complete live enforcement
union determine the current route. Other consumers are not automatically opted
into a queue, and this instruction change does not migrate Pack CI itself.

Use three distinct states:

- **Legacy protected route:** use the installed request and final merge procedure
  until its replacement is qualified; do not invent a queue command.
- **Queue migration:** stage and qualify the replacement under its existing
  controller while preserving enforceable proof on the old route.
- **Verified queue route:** product/scope/merge authorization precedes enqueue;
  passing current integration proof permits native protected landing.

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
| G | The native merge-group commit/tree | The integration composition being considered for landing |
| M | The actual landed commit/tree | What reached the target branch |

Retain tested source, commands, toolchain/policy identities, run/attempt,
selected obligations, actual outcomes and accessible original evidence. Reused
proof keeps its original identity. H is not G; a successful control workflow on
main is not automatically proof for an input SHA. Squash commit identity may
change; compare the corresponding tested and landed tree, not commit equality.
For cumulative groups, reconcile the correct landed prefix rather than assuming
that the first landed PR has the final group's tree.

A G identity does not itself provide its complete constituent PR/head list.
The public merge-group payload provides base/head identities, not a member list.
Associated PRs, a queue-ref name, commit timestamps and a current queue prefix
are not an immutable membership receipt. Do not manufacture that binding.

A consumer requiring constituent metadata must establish either authoritative
membership or a reviewed admission-equivalence contract enforced for every
native entry path. The latter must bind exact H, producer, policy and mutable
metadata and handle head/title/label changes, review withdrawal and bypasses.
A matching check name or signed guessed membership does not establish it.
Perl's [#18255 owner reconciliation](https://github.com/EffortlessMetrics/perl-lsp-swarm/issues/18255#issuecomment-6338272679)
records this unresolved integration seam and preserves the #16017 title writer.

## Selected lifecycle

```text
local implementation and focused proof; Draft publication starts no CI
-> substantive review and joined repairs
-> current product/scope judgment and authorization for exact H
-> explicit admission and native enqueue
-> one applicable qualification transaction on G
-> native protected landing if all current required conditions hold
-> cheap M reconciliation and acceptance update
```

Enqueue authorizes automatic landing on successful proof. It is not a neutral
request for tests. Source changes or a material adverse finding withdraw
eligibility and require affected review/proof before re-entry. A new finding
at unchanged H must still be able to stop landing. Keep the candidate owner
accountable while doing independent work instead of polling. Qualification does
not require another routine approval after green.

## GitHub constraints that determine the design

GitHub couples PR and merge-group required checks: the required contexts must
be satisfied before enqueue and must also report on G. The final design therefore
needs real exact-H admission context publication plus applicable G proof,
protected by enforced queue-only landing. Admission publication is an explicit
operation at the admission boundary, not an automatic PR-event CI workflow.
Its approved producer and expected application binding are implementation and
native-acceptance obligations; a worker assertion is not sufficient.

The bounded migration bootstrap is different: existing full PR qualification
continues to publish the required admission contexts, and current exact-H source
review and conditional merge authorization remain prerequisites to enqueue.
The cheaper explicit publisher replaces that full producer only in step 5;
it does not leave an admission-free window or weaken the bootstrap's proof.

Never change a protected PR result from qualification to admission while direct
landing can still consume it. Every required context needs a valid G disposition,
including metadata checks. A skipped job, missing result, unconditional success,
wrong subject/app, cancelled work or never-executed required child cannot pass.

Build concurrency limits simultaneous queue builds. Merge min/max settings
control landings, not build batching or immutable membership. Begin a bounded
canary with concurrency 1, one-entry landing, squash and all entries required
to pass. These settings alone do not prove a singleton build. A controlled
singleton observation also excludes other admissions/in-flight groups and
captures actual B/G/H evidence; it cannot establish multi-member acceptance.
Increase concurrency from measured pass rate, invalidation cost, arrival rate
and capacity. A 35-minute serial lane has a no-failure ceiling of about 1.7
entries/hour, before overhead.

Target normally <=20 minutes of complete active qualification, including setup,
children and finalization. Measure queue wait separately and preserve all failed,
retried, cancelled, local and review costs. Finite status timeouts come from
observed valid runtime, not permission to call a long run efficient.

## Safe activation and rollback

1. Inventory source, all applicable classic/ruleset controls, protected contexts
   and producer bindings, runner trust, cache writers and active runs. Checked-in
   desired configuration is not live enforcement.
2. Implement G evaluation and explicit admission, including actual checkout
   identity, metadata/membership or admission equivalence, review withdrawal and
   complete proof. Prove cold dependency preparation independently of cache hits.
3. Rehearse the source and failure controls under non-required identities. Keep
   the old required proof available. Synthetic fixtures are not native G evidence.
4. Through the existing authorized settings owner, enable and read back queue
   enforcement for a bounded bootstrap. Full legacy PR qualification supplies
   the required entry contexts; current exact-H review and conditional merge
   authorization are also required before enqueue. Observe the first actual
   native G transaction here, not as a circular prerequisite to writing its
   producer. Record temporary duplicate costs.
5. After queue-only landing and every protected producer are demonstrated,
   replace full PR qualification with the qualified explicit admission publisher
   and remove ordinary PR-event CI, including cheap wrappers, plus duplicate
   broad main-push work. Sweep callable children and indirect callers. Keep
   distinct incident/deep/release obligations.
6. Record native entry, actual G proof, protected M and matched readback. Verify
   zero CI starts for ordinary Draft/Ready/update events and inspect the first
   operating cohort for false passes, false blocks, queue age and accepted-change cost.

Rollback pauses new admissions, reconciles in-flight work and restores the full
protected PR qualification path first. Verify it before removing queue-only
enforcement. Never allow admission alone to authorize direct landing. Restore
one coherent producer/settings/cache generation. A documentation rollback alone
changes no live rule.

## Main health and repairs

A confirmed main-health incident has one accountable integration owner, not a
permanent polling thread. Parallel diagnosis is useful; competing repair,
revert and dependency-repin writers are not. Pause ordinary queue admission and
qualify the designated repair without bypassing protection or requiring already
repaired main. A queue cannot fix hidden fixture dependencies, flaky tests or a
wrong test oracle.

After M, reconcile identity and the smallest useful landed behavior. Do not
replay the full suite merely because a push occurred. Preserve independently
admitted incident, release and deep checks and the separately governed main-health
cadence. A merge does not authorize publication, upstream promotion or release.

## Discriminating consumer acceptance

These are consumer observations to establish, not tests executed by this document.

| Case | Required result |
|---|---|
| Ordinary Draft/Ready/update event | Zero CI workflow starts; local work continues |
| Explicit exact-H admission | Genuine proof/review validation and approved context publication, not a success shim |
| Individually green PRs interact incorrectly | Current combined G fails before the incompatible composition lands |
| Old P is green after relevant base movement | It cannot substitute for G |
| H changes after review/admission | Old authority is not inherited |
| Material finding arrives at unchanged H | Withdraw eligibility; preserve historical test facts |
| Title/label changes without H movement | Revalidate affected mutable admission metadata |
| Membership is inferred from association/ref/time | Refuse the claim; no invented constituent coverage |
| Protected metadata context has no G producer | Activation refuses rather than leaving a permanently waiting queue |
| Required child is absent, skipped, wrong-app/SHA/attempt or never starts | No successful qualification |
| Warm cache hides a fixture dependency | Cold preparation exposes and repairs the contract |
| Predecessor fails or leaves the queue | Recomposition has new identity and affected qualification |
| Duplicate request or lost response | Reconcile the existing native operation before retry |
| Main is red with an accepted repair | One owner can qualify it without bypass or circular prerequisites |
| G passes but M does not correspond | Landing incident, not completed acceptance |
| Rollback during active work | Restore full PR proof before permitting direct landing |
| Consumer still uses the legacy route | Report and use actual installed behavior until qualified cutover |

Primary contracts: [Managing a merge queue](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-a-merge-queue),
[merge-group payload](https://docs.github.com/en/webhooks/webhook-events-and-payloads#merge_group),
[queue entries](https://docs.github.com/en/graphql/reference/pulls#mergequeueentry),
and [ruleset settings](https://docs.github.com/en/enterprise-cloud@latest/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets#require-merge-queue).

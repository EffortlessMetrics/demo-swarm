---
name: flow-1-signal
description: Investigate the problem, challenge its premises, and define testable behavior and scope.
argument-hint: "[optional-run-id] <feature request or signal>"
---

# Flow 1: Signal -> Spec

Turn the signal into an investigated problem and a falsifiable acceptance claim.
The accountable owner can research, inspect source, frame requirements and review
them in the same useful session. Specialists are optional capabilities, not a
required roster. Keep the useful reasoning order without reconstructing an
assignment that already has current source, decisions and evidence.

## Enter from current state

From repo root, resolve the governing issue or accepted request and inspect its
current candidate, production consumers, dependencies, relevant decisions and
prior findings. Prefer the existing coherent owner/candidate over duplicate work.
An issue is a starting claim, not a guarantee that its diagnosis or proposed fix
is correct. Apply zero trust development and fallibilism.

Use existing evidence with its scope and provenance. Investigate unsupported
load-bearing premises, relevant changes, contradictions and plausible alternatives.
A current specification can be wrong; preserve accepted intent while correcting
the factual premise or proposing the better implementation. A change to
non-derivable product direction needs the owner's decision. Ordinary investigation
and authorized correction do not need another permission round-trip.

A useful order is:

1. Establish what users or production consumers experience and why it matters.
2. Check the proposed cause and mechanism against current source, specifications,
   documentation, prior work and the strongest plausible counter-read.
3. Define intended behavior, boundaries, failure cases and material constraints.
4. Identify the observation or proof that distinguishes the current defect or
   missing behavior from a correct implementation.
5. Challenge scope, compatibility, dependencies, risks and the cost of obtaining
   that proof; reconcile the conclusion and next action.

Return to an earlier question when evidence changes its premise. Reuse the same
session or a context-preserving fork for a new angle by default. Add a separate
reviewer when its method, evidence or perspective justifies the context cost.
Neither an earlier clean report nor a different actor name settles the question.

## Make acceptance discriminating

Specify what must be observably different and what remains outside the claim.
For behavior changes, prefer a red/green demonstration at the real consumer.
Before implementation, explain which defect or realistic wrong behavior should
fail and why. If literal red/green is unavailable, identify the limitation and a
meaningful negative control, differential result, model or other falsifier.

Keep the proof obligation distinct from its recurring schedule. A useful full
reproduction may belong in a deeper tier while a focused regression protects the
ordinary path. Do not remove the discriminator to make a test cheap, or require
every broad test on every edit.

Use the consuming repository's established requirement, contract and test forms.
Gherkin, REQ/NFR identifiers and BDD examples remain available when applicable;
they are not mandatory new artifact sets for every signal. Identify affected
stakeholders and material risk at the depth the claim needs.

## Retain current knowledge and helper compatibility

GitHub owns current issue/candidate/findings state; Git owns versioned intent
and source. Record material conclusions, contrary evidence, changes of premise,
reasons, remaining uncertainty and the next useful action at those owners.
Do not mirror live state into a mandatory tracked checklist or heartbeat log.

Existing local run artifacts under `.runs/<run-id>/signal/` can preserve evidence.
Use them when an actual helper or downstream consumer needs their interface;
do not fabricate historical artifacts to make a flow appear complete. A file
that exists or "looks current" is not proof that its claims remain applicable.
An inaccessible sender-local path is not proof that the artifact does not exist.

For callers that need the existing run interface:

- `gh-issue-resolver` supplies the issue/run binding; preserve an existing valid
  binding. `run_id_kind: LOCAL_ONLY` and `issue_binding: DEFERRED` retain their
  native meanings. A repository/trust block is not temporary missing GitHub access.
- `signal-run-prep` establishes the local run directory and `run_meta.json`.
  Do not read not-yet-created local files as if they were missing execution proof.
- `repo-operator` handles authorized branch/checkpoint operations with narrow
  staging. Preserve existing work and unrelated staging; a naming convention
  does not require a new branch or writer.
- Existing requirements, examples, risk notes and `signal_receipt.json` keep
  their consumer schemas. `signal-cleanup` derives required counts from actual
  evidence and reports unknown/missing input honestly.
- Reseal-if-modified applies to a receipt whose inputs changed. Preserve
  unaffected evidence and diagnose repeated failure rather than retrying without
  new information. A non-convergent reseal retains the actual failure and next
  action; do not invent helper fields or fabricate counts. If context is exhausted,
  checkpoint the claim and evidence so continuation need not reconstruct the work.

`gh-researcher`, `signal-normalizer`, `problem-framer`, `clarifier`,
`requirements-author`, `requirements-critic`, `bdd-author`, `bdd-critic`,
`scope-assessor`, `risk-analyst` and `spec-auditor` are available bounded
implementations. Give a delegate the actual relevant source, question and evidence
it needs; do not assume its harness inherited every rule. The owner joins its
findings against evidence rather than treating "ready" as automatic approval.

## Publication and continuation

Inspect the installed publication route first. The selected steady state starts
no CI on ordinary commits, pushes, Draft or Ready. Signal investigation does not
request integration CI. An existing route that still starts CI is a migration
constraint; use its approved procedure without bypassing controls.

When publishing source or run evidence, retain the useful dependency order:
applicable cleanup, `secrets-sanitizer` on the actual publication surface,
`repo-operator` for authorized narrow commit/push, then permitted GitHub updates.
These are controls, not compulsory new agents. Respect `safe_to_commit`,
`safe_to_publish`, `proceed_to_github_ops` and `publish_surface` within their
existing scopes. They do not grant broader publication authority.

Issue-first: `gh-issue-manager` and `gh-reporter` update the governing issue with
material decisions and evidence when authorized. A failed source push may still
permit a sanitized restricted handoff; it cannot establish remotely available
source. A no-op requires no empty commit. Read back consequential remote effects
before reporting them as complete.

The useful exit is an investigated problem, scoped intended behavior, a credible
discriminator, material uncertainty and a next action. It may be a bounded plan,
correction of the issue, continuation of an existing candidate, or an
evidence-backed conclusion that the requested work is already delivered,
superseded or mis-scoped. Artifact existence, a posted summary and a child's
return do not by themselves establish that outcome.

Proceed to `/flow-2-plan` only when further design work is useful; otherwise
continue at the earliest missing judgment. Ask for a decision where intent,
exposure, authorization or an irreversible effect actually requires it. Human
input can arrive during the work; apply it to the affected conclusions. A partial
checkpoint retains the evidence, remaining gap and exact next action without
claiming the larger objective complete.

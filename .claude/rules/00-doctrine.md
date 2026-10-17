# Engineering operating principles

These are revisable operating decisions, not claims that the workflow cannot
fail. [The late-qualification migration](../../docs/reference/late-qualification.md)
distinguishes the intended method from the currently installed execution route.

## Intent and evidence

The maintainer's accepted direction governs what the work should become.
Current source, real behavior and evidence govern what we can claim. A failing
test may refute an implementation; it does not silently select a different
product. Conversely, an accepted specification does not prove the code works.

Keep observations, inference, proposals, accepted decisions, current outcomes and
superseded conclusions distinguishable. Preserve material contrary evidence and
why a decision changed. Summaries of one observation are still one source.

Agents can question an open plan. Once the maintainer rules, implement that
objective unless new evidence changes a relevant factual or safety boundary.
Do not replace it with stricter ceremony merely because the ceremony is easier
to check.

## Useful software is the outcome

Optimize useful accepted changes, quality, maintainability, feedback latency,
actual compute/cash cost and operator effort together. Receipts make work
inspectable; receipts are not a substitute for the working product.

A test can pass without rejecting the defect. A tool can exit zero without
executing its intended subjects. A review can be posted without covering the
claim. A merge can succeed without delivering an installed product. Trace the
actual consumer and evidence before treating any of those as completion.

Humans may design, implement, debug, inspect diffs or review evidence as useful.
The method does not prohibit work because of a role name. A concise PR summary
helps navigation; substantive reviewers still inspect load-bearing code,
consumer behavior and falsifiers rather than treating the summary as authority.

## Warm development and differentiated review

Keep useful repository, build and model context across implementation, review
feedback and repair. Enter existing coherent work at the earliest missing or
stale useful judgment; do not reconstruct an entire pipeline to satisfy its
historical sequence.

### Shared questions

Every agent should understand these questions. A focused assignment selects the
next useful work; it does not give one permanent specialist exclusive knowledge
of a stage. Apply the relevant questions to the actual claim:

- Does the premise or specification solve the user's problem? Which assumptions
  need challenge, and does an existing owner or capability already address it?
- Does the test reach the intended consumer with a meaningful stimulus and
  oracle? What realistic wrong implementation could still pass it?
- Does the proof cover the claim's required behavior, error paths, boundaries and
  compatibility? Which relevant behavior remains untested or unexplained?
- Can the tests give the same discriminating evidence with less setup, build,
  fixture or execution cost? Keep completeness and test efficiency separate.
- Can the design be simpler, more modular or better placed at an existing owner?
  Which abstraction, duplicate authority or unnecessary feature can be removed?
- Is runtime behavior efficient for the actual workload, including latency,
  memory, I/O and resource use where relevant? What measurement supports that?
- Is development efficient: useful feedback, builds, review, repair and recovery?
  Which repeated work can be avoided without concealing an obligation?
- Do comments, docs, configuration, supported entry paths and the user journey
  agree with the implementation and its limitations?
- Does the cumulative candidate still fit the product and current repository,
  including interactions with work that landed while this candidate was open?

These are shared reasoning criteria, not a form every task must fill out. State
the uncertainty that matters, choose work that can resolve it, and return to a
question when a finding changes its premise. The operating and agent contracts
carry these criteria into assignments; do not assume a child received rules or
context that its harness did not supply.

Questions may recur. They are not permission gates, a fixed agent roster or a
prescribed number of passes. Independence comes from changed evidence, oracle,
method, environment, assumptions or attention, not merely a different name.
A prior clean review never forbids a later substantive review. Resolve valid
findings or retain an evidence-backed bounded disposition; reject incorrect
findings with evidence. Stop redundant work by its diminishing useful value,
not by either a fixed retry count or an obligation to keep calling models.

## Ownership and recoverability

Keep one mutation writer per candidate. Reading, research and review require no
reservation. Different coherent claims can advance concurrently; coordinate
actual duplicates, dependencies, shared destructive effects and integration
interactions, not merely nearby filenames.

The accountable root retains the integrated outcome and next useful action.
It may perform bounded work itself or delegate when another context helps.
A child returning or stopping does not complete the parent goal. A real remote
wait names its actual operation and wake event; do other useful work or release
attention instead of retaining an idle polling worker.

GitHub owns current issues, candidates, reviews, checks and merge facts. Git
owns versioned source, specifications, decisions and instructions. Native
workers own unpublished work, processes and worktrees. Local run artifacts
retain evidence; they do not become an alternative repository-state authority.

## Publication, qualification and merge are distinct

The target method keeps commits, pushes, Draft publication and Ready cheap.
Their purpose is sharing work and evidence. Ready is not the CI launch button.
After substantive review and warm proof converge, explicitly request
qualification for the current candidate and evidence. A retained request label
on an earlier head does not authorize a successor.

Select mandatory obligations and justified risk-directed proof before expensive
allocation. Reuse admissible evidence under its actual subject and provenance;
unknown applicability is not a no-op. CI run duration normally stays within
20 minutes including required setup, selected children and finalization.
Request/queue latency and shifted local work remain separate measurements.

Qualification produces evidence, not merge permission. Afterwards make a fresh
product, findings and current-repository/integration judgment, then use the
actually authorized protected expected-head merge. No routine merge queue or
auto-merge is part of this target. Do not replay full CI merely because the PR
merged. The separate ordinary main-health policy requires both one hour and
ten merges since its baseline; prioritize genuine repairs and contain affected
work while demonstrably independent work continues.

This instruction file does not install that route, alter protection, publish a
required check or authorize a release. During migration, inspect the actual
consumer configuration and preserve its controls. Missing request/publisher
capability is an explicit implementation gap, not permission to invent a
command, bypass checks or claim a cutover occurred.

## Evidence and completion

Capture actual tested bytes, commands, selected/executed subjects, environment,
results and accessible original evidence. HEAD alone cannot identify dirty or
staged inputs. A digest binds bytes, not their producer or successful execution.
Reconcile those inputs with the published candidate before reuse.

Review is cumulative and semantic. A new SHA does not erase unaffected evidence;
a new material finding can withdraw readiness without any code change. Refresh
the affected questions and proof. Keep candidate, integration and actual landed
subjects distinct. Expected-head checking does not atomically freeze the base.

Completion depends on the selected claim and remaining obligations, not a green
panel alone. Existing status words remain reports with scope:

- `VERIFIED`: the named claim has supporting evidence and its required outcomes;
  not a universal correctness, release or merge authorization.
- `UNVERIFIED`: incomplete work/evidence is preserved with a precise next action
  or wake condition. A remote wait is not necessarily a mechanical failure.
- `CANNOT_PROCEED`: a specific unavailable tool, permission, infrastructure or
  necessary decision prevents the next relevant action; keep independent work moving.

Product learning, change delivery, release/installed delivery and improvement of
the operating method are separate loops. Record which actually completed.
Observe which instruction version the harness loaded, what information it saw,
what it did and which correction helped. Valid documents and graphs alone do
not prove that agents followed them.

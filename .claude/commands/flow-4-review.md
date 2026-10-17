---
name: flow-4-review
description: Investigate the candidate, disposition current findings, and verify repairs before explicit qualification.
---

# Flow 4: Review and repair

Produce substantive current review of the actual candidate. Review is more than
harvesting comments: inspect the claim, source, production consumers, proof and
credible counterexamples even when no bot has posted anything.

## Current inputs

Read the controlling issue, current candidate/head/base, actual review threads,
material prior decisions and accessible original proof. Existing build/review
artifacts are useful history, not live authority. Do not pre-mark a finding
resolved because a file exists or a former review was clean.

A Draft is reviewable. Creating a missing PR must use the repository's safe
publication route; it is not a reason to launch independent qualification.
Neither source review nor a review-complete conclusion requires future CI green.
Existing failures still matter and must receive a disposition within their scope.

## Investigate and join findings

Ask what each change means to real consumers, which wrong behavior the tests
reject, whether exceptions/error paths and compatibility are supported, and
whether test cost, complexity, docs and product direction remain sound. Select
tools and additional readers to vary the evidence or questions, not to fill a
fixed roster. The root joins conclusions, not votes.

Harvest current human, bot and tool feedback through existing adapters when
useful. Preserve original finding/thread identities and contradictory evidence.
Read every available page of reviews, discussion and inline comments, and native
thread resolution state. Unknown/truncated feedback stays incomplete rather than
clean. A MAJOR finding can require immediate repair; Build does not postpone it
merely because it is below CRITICAL.

Cluster for efficient repair without collapsing different causes or losing
attribution. Distinguish implementation defects, weak proof, instrument failure,
unsupported claims and suggestions.

Verify every material finding against current source. A shifted line or new SHA
alone does not refute it. Send accepted repairs to the candidate writer; refresh
only affected tests, oracles, consumers and judgments. Re-read the changed code
and actual proof before recording Fixed. A resolved thread or author response
is not proof of repair.

Reject incorrect findings with evidence. Valid deferred findings need a durable
follow-up and an explicit acceptance disposition; calling an issue small or
nonblocking does not resolve it. Novel scope belongs in a separate claim unless
it is necessary to complete the current acceptance.

A prior clean review never suppresses a later substantive pass. Stop redundant
passes by diminishing useful value, not a minimum number of clean reports.
Keep warm context and avoid repeating full analysis for unrelated edits.

## Close the useful loop

Record the current claim/candidate, evidence examined, methods and limitations,
material findings and their dispositions. Use existing review/worklist schemas
where needed, but do not invent counters or replace GitHub's live state with
tracked files. The PR summary is navigation, not a substitute for source review.

For each original thread, distinguish verified repair/refutation from GitHub's
conversation state. After checking source and affected proof, the authorized
owner replies with the disposition and evidence, then resolves the exact native
thread when the disposition and repository policy permit. Use the thread node
ID, not the numeric review-comment ID. Read back the resolution; a reply, local
RESOLVED item, changed line or outdated flag does not perform that operation.
Never bulk-resolve unread threads or resolve only to make a gate green. Keep a
valid outstanding or unaccepted deferred finding open. Grouping findings never
resolves every child automatically. Lack of resolution permission is a named
capability blocker, not a reason to request broader credentials or repeat writes.

Re-fetch native threads and reviews after repairs and before final integration
to catch new material feedback. This decision may be performed by the existing
owning lead; it does not require a new agent or routine human approval. Do not wait in an idle polling worker for a bot; preserve
its native operation and wake condition when that is the actual dependency.
Do independent useful work or checkpoint.

`pr-feedback-harvester`, `review-worklist-writer`, reviewers, the current writer,
`test-executor`, `pr-commenter` and cleanup helpers remain optional bounded
implementations. A specialist's old global instruction does not override this
flow's current lifecycle or grant additional mutation authority.

## Exit

When substantive review is current, required local proof is sufficient and
material findings have evidence-backed dispositions, continue to
`/flow-5-gate` for selection and an explicit qualification request. Several
reviewed alternatives do not each require expensive CI; the root selects the
candidate intended to land for the objective first. Record independent CI as
NotRun when it has not run. Do not toggle Draft/Ready to start it.

Readiness metadata may be changed only for its real review purpose under the
installed safe route; it is neither qualification nor merge authorization.
New findings return to the affected Build/Plan question. A blocked instrument
or genuinely unresolved owner decision retains a precise next action.

Behavioral acceptance cases: [review continuation](../../docs/reference/review-continuation-cases.md).

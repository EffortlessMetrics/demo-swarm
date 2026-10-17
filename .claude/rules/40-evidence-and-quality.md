# Evidence and quality

Evidence supports a claim about useful software. A PR summary helps readers
find source, findings and proof; it does not replace substantive investigation
or make a green panel the product. Apply the
[shared engineering questions](00-doctrine.md#shared-questions) throughout the
work, including premise, test oracle, completeness, efficiency and product fit.

## Bind observations to what happened

Retain the actual source or immutable input identity, command and environment,
selected and executed subjects, result, capture limitations and accessible
original evidence. A dirty or staged run needs those bytes; HEAD alone cannot
identify them. A hash binds bytes but does not authenticate a producer or prove
execution. A sender-local path is not a completed handoff to another worker.

Distinguish product failures, instrument failures, missing evidence, proven
inapplicability and work that has not run. A zero exit from a wrapper does not
turn failed, skipped or absent children into successful proof. Preserve partial
success and interruption honestly without calling the interrupted whole a pass.

Tests need a relevant stimulus, actual consumer and discriminating oracle.
Passing a test that also accepts the realistic defect is weak evidence. Coverage
or a generated file can identify where to investigate; neither alone proves
correct behavior, completeness or delivery.

## Historical truth and present applicability

An observation remains evidence about its original subject. Separately assess
whether it supports the current claim. Review source, dependencies, environment,
selected obligations, findings and intended use at the scope that can affect it.

| Change or observation | Useful response |
| --- | --- |
| New SHA with an unrelated edit | Preserve original evidence and explain why its subject remains applicable. |
| Material source, dependency, environment or oracle change | Refresh affected proof and its consumers; retain unaffected evidence. |
| New material finding on the same head | Investigate and reconsider readiness even if earlier tests passed. |
| Unknown impact or unavailable original inputs | Name the gap; inspect, widen the relevant proof or keep the affected claim unproved. |
| H1 request followed by H2 | Preserve H1 results; do not treat that request or its status as an H2 qualification. |

Do not rename old evidence as a current-head execution. Equally, do not erase a
valid observation merely because HEAD moved. Existing helper status fields and
receipt schemas remain unchanged; explain subject and applicability alongside
them instead of inventing counters, silently rewriting history or using SHA
equality as universal semantic currentness.

Dependency-cache reuse, compiler-artifact reuse, test-result reuse and semantic
review are separate decisions. A reusable build directory does not establish a
passing test, and an applicable review does not supply a missing required check.
Use the consumer's actual admission and proof rules for consequential effects.

## Review the engineering claim

Inspect load-bearing code, real entry paths, tests and credible counterexamples.
Ask whether the specification and design serve the user before spending effort
proving the wrong behavior. Simplification, modularity, supported compatibility,
documentation and product direction remain review questions even after tests
are green. A fixed set of metrics or spot-check count cannot answer every claim.

Choose further criticism by the uncertainty or failure it could expose. Vary
the evidence, method, oracle, assumptions or attention where useful. A changed
role name or repeated clean result alone does not establish independence.
Preserve native independent-review requirements and disposition new material
findings even when an earlier review was clean.

## Account for quality and cost together

Keep runtime efficiency, development efficiency and test efficiency distinct.
Measure relevant product workloads and resources; inspect build, feedback,
review and recovery costs; make repeated tests inexpensive while preserving
their discrimination and required coverage. More compute or more review passes
can be useful, but their value must follow the question they answer.

Preserve the complete qualification boundary and timing in
[the current doctrine](00-doctrine.md#publication-qualification-and-merge-are-distinct).
Queue delay, total machine occupancy and work shifted into warm sessions are
separate measurements. A faster component or warm run does not establish a
faster complete route. Do not weaken an oracle, omit an obligation or hide setup
to meet a timing target.

## Completion and next action

Use `VERIFIED`, `UNVERIFIED` and `CANNOT_PROCEED` with the scope defined by
[CLAUDE.md](../../CLAUDE.md). A source-review conclusion can be complete while
future qualification is NotRun; do not create a CI-before-review cycle. Source
review also does not grant a missing qualification result or merge authority.

Complete qualification supplies evidence for a separate final decision over
current findings, integration, applicability and product intent. The same
authorized lead can make that decision with fresh inputs. A required check,
resolved thread or green panel alone does not perform it. Protected merge and
actual landed reconciliation remain distinct from release or installed delivery.

Make the successor's work clear: what claim is supported, which original
evidence supports it, what changed, what remains uncertain and the next useful
action or actual remote wake condition. Reuse native issue, PR, review and check
records; local evidence does not become a second live-state authority.

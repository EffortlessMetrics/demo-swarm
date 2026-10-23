# Intent to narrative

Keep intended behavior, candidate implementation, evidence, decisions and the
summary distinguishable. They answer different questions; one universal ranking
cannot resolve every disagreement between them.

## From intent to a reviewable decision

1. **Intent:** identify the accepted problem, requirements, contracts and scope.
   Distinguish accepted direction from proposals and assumptions. An issue may
   describe the wrong cause or suggest an inferior implementation; challenge
   those claims without silently changing the maintainer's intended outcome.
2. **Candidate:** inspect the implementation, tests, configuration and actual
   consumers. Work remains provisional until the applicable claim is supported.
3. **Evidence:** use attributable observations, test results and substantive
   findings. Check what the instrument selected and executed, its oracle, source
   identity and limitations. An exit code is an observation, not a correctness
   certificate. Deterministic extraction can also be wrong.
4. **Decision:** the accountable owner weighs evidence and unresolved findings
   under the installed integration route. Review, qualification, merge and
   release have different authority and completion conditions.
5. **Narrative:** explain the result, material reasoning, contrary evidence,
   limitations and next action. Link to original evidence and load-bearing code.
   A summary helps readers navigate; it does not replace the underlying review.

These are revisitable reasoning steps, not a fixed actor pipeline. The same
useful session can investigate, implement, challenge and integrate. Use a fork
or separate reviewer where its additional evidence or viewpoint earns its cost.

## Zero trust development

Fallibilism applies to every layer. A recorded failing execution refutes an
unqualified claim that that execution passed. It does not by itself establish
whether the defect is in production code, the test, instrumentation or its
environment. A successful execution can still miss the relevant behavior.

Use the strongest applicable original evidence for a factual claim and current
accepted direction for intent. Investigate conflicts at the relevant seam,
preserve contrary evidence, and version material corrections with their reasons.
Do not restart every check because a new question or unrelated edit appeared.
Historical results retain their subjects; present applicability is a separate
judgment. See [truth-hierarchy.md](../../docs/explanation/truth-hierarchy.md).

## Review and compression

Choose review depth from the claim, failure consequences and remaining uncertainty.
Inspect load-bearing code, test oracles, consumers and credible wrong behavior.
A large PR is not made safe by compressing its description, and small PRs are
not automatically efficient. Prefer coherent acceptance and rollback boundaries.

Summaries should let the next worker resume at the earliest unresolved question.
Include the candidate, what changed, useful proof, material findings, limits and
next action. Keep detail accessible rather than copying it into every handoff.
Do not invent universal line-count, review-time or compression savings.

## See also

- [00-doctrine.md](00-doctrine.md) — Current operating principles
- [60-flow-orchestrators.md](60-flow-orchestrators.md) — Context reuse and integration
- [claims-and-evidence.md](../../docs/explanation/claims-and-evidence.md) — Evidence records

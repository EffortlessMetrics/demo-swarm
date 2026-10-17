# Pack CI token and checkout policy

The hardening from #25/#26 is checked in the existing Pack CI lint job. From the
repository root:

```bash
python -m pip install -r scripts/requirements-ci.txt
python scripts/check_pack_workflow.py
python -m unittest discover -s scripts/tests -p 'test_*.py' -v
```

The checker reads the actual `.github/workflows/pack.yml` by default. Use
`--workflow PATH` to inspect another local source file. It does not modify the
workflow, install tools, call GitHub, emit a protected status or run product code.
Exit 0 means the declared policy passes, 1 means a configuration violation, and
2 means the file could not be read or interpreted. Missing dependencies also
fail execution; they do not yield a passing policy result.

## Checked boundary

The workflow explicitly grants only `contents: read`. Job overrides may reduce
that grant but not widen it. Each explicit proof job must have an inspectable
`actions/checkout` step, and every checkout must set `persist-credentials: false`
without a separate token or SSH key. New jobs and later checkout steps receive
the same checks; the checker does not freeze a seven-job inventory.

The parser preserves scalar keys such as `on`, rejects duplicate keys, and
refuses aliases/merge keys rather than guessing their effective authority.
Reusable jobs are outside this local checker and require an explicit adapter
review. These are supported-input limits, not a claim that all such YAML is
invalid on GitHub. This is not a complete Actions schema or syntax validator.

Tests exercise positive configurations and altered workflow inputs, every
current checkout, later/mixed-case checkouts, job overrides, malformed/ambiguous
source, empty proof graphs, CLI exit codes, read-only behavior and the actual
lint-job invocation. They call the production parser and checker, not a copied
policy predicate. Future legitimate workflow changes are not rejected merely
because they differ from an old byte-for-byte snapshot.

## Native evidence remains separate

The initial hardening was independently executed in
[Pack CI 39021571790](https://github.com/EffortlessMetrics/demo-swarm/actions/runs/39021571790).
Its [lint log](https://github.com/EffortlessMetrics/demo-swarm/actions/runs/39021571790/job/117364268377)
records Contents/Metadata read access and Git authentication removal before
repository scripts. All ten jobs passed; #26 landed as `ed423547`.

This source check does not establish absence of secrets in arbitrary actions,
transitive action behavior, runtime/cache credential containment, resistance to
a candidate changing the checker itself, or live repository protection. It does
not choose proof obligations or qualification events. Triggers, matrices, audit
and product tests retain their own contracts. #22's late-qualification migration
and actual harness adoption remain distinct work.

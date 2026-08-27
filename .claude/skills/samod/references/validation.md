# SAMOD validation — running the three tests

SAMOD's three tests (Model, Data, Query) have a *formal* (computable) part and a *rhetorical* (human-reviewed) part. This file covers the formal part only.

Assumptions: venv active (`source scripts/venv/bin/activate`), commands run from repo root.

---

## Model test — TBox consistency

Parse-only check (catches syntactic and most structural errors):

```bash
python - <<'PY'
from rdflib import Graph
g = Graph()
g.parse("development/NN/TBOX.ttl", format="turtle")
print(f"OK — {len(g)} triples parsed")
PY
```

For DL consistency (OWL reasoning), open the TBox in Protégé and run HermiT / Pellet — rdflib alone does not reason. A minimal programmatic approximation using `owlrl` (RDFS/OWL-RL closure, not full DL):

```bash
pip install owlrl  # once, in the venv
python - <<'PY'
from rdflib import Graph
import owlrl
g = Graph()
g.parse("development/NN/TBOX.ttl", format="turtle")
owlrl.DeductiveClosure(owlrl.OWLRL_Semantics).expand(g)
print(f"Expanded to {len(g)} triples")
PY
```

If closure fails or grows unexpectedly (e.g. every class becomes `owl:Nothing`), you have an inconsistency — inspect the latest TBox edit.

---

## Data test — TBox + ABox consistency

Same approach, loading both:

```bash
python - <<'PY'
from rdflib import Graph
g = Graph()
g.parse("development/NN/TBOX.ttl", format="turtle")
g.parse("development/NN/ABOX.ttl", format="turtle")
print(f"OK — {len(g)} triples after loading TBox + ABox")
PY
```

Rhetorical side: open `motivating-scenario.md` and `ABOX.ttl` side by side and answer, for each Example:

- Is every fact stated in the Example present as a triple in the ABox?
- Is every individual typed?
- Does the ABox reveal any TBox gap (a property you want to assert but that doesn't exist)?

---

## Query test — SPARQL answers the CQs

Extract the SPARQL blocks from `formal-competency-questions.md` and run each against the merged graph.

One-shot script (drop into `scripts/run_cqs.py` if you want to keep it):

```python
#!/usr/bin/env python
"""Run every SPARQL block in an iteration's formal-competency-questions.md."""
import re, sys
from pathlib import Path
from rdflib import Graph

def extract_queries(md_text: str):
    # Matches ```sparql ... ``` fenced blocks.
    return re.findall(r"```sparql\s*(.*?)```", md_text, flags=re.DOTALL)

def main(iter_dir: Path):
    g = Graph()
    g.parse(iter_dir / "TBOX.ttl", format="turtle")
    g.parse(iter_dir / "ABOX.ttl", format="turtle")

    md = (iter_dir / "formal-competency-questions.md").read_text()
    queries = extract_queries(md)
    print(f"Found {len(queries)} queries in {iter_dir.name}")
    for i, q in enumerate(queries, 1):
        try:
            rows = list(g.query(q))
            print(f"  CQ #{i}: {len(rows)} rows")
            for row in rows[:5]:
                print(f"    {row}")
        except Exception as e:
            print(f"  CQ #{i}: FAILED — {e}")

if __name__ == "__main__":
    main(Path(sys.argv[1]))
```

Usage:

```bash
python scripts/run_cqs.py development/NN
```

Rhetorical side: compare the rows against the *Expected result* block under each CQ. A query that returns *something* but not the expected rows still fails the query test.

---

## Phase 2 — formal tests across the whole BoT

After `merge_iterations.py` runs, iterate over every iteration and rerun the three tests. Quick loop:

```bash
for d in development/[0-9][0-9]; do
  echo "=== $d ==="
  python - <<PY
from rdflib import Graph
g = Graph()
g.parse("$d/TBOX.ttl", format="turtle")
g.parse("$d/ABOX.ttl", format="turtle")
print(f"{len(g)} triples")
PY
done
```

Any iteration whose ABox references an entity renamed during the merge will fail to produce expected CQ rows — fix that iteration's ABox / SPARQL to the new names.

---

## Consolidated ontology check

After `merge_iterations.py`:

```bash
python - <<'PY'
from rdflib import Graph, OWL, RDF
g = Graph()
g.parse("ontology/triple.ttl", format="turtle")
classes = set(g.subjects(RDF.type, OWL.Class))
op = set(g.subjects(RDF.type, OWL.ObjectProperty))
dp = set(g.subjects(RDF.type, OWL.DatatypeProperty))
print(f"Classes: {len(classes)}  Object properties: {len(op)}  Data properties: {len(dp)}")
PY
```

Cross-check the numbers against `CHANGELOG.md` to confirm the merge did what you expected.

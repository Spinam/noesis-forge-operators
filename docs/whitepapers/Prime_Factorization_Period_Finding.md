# Prime Factorization — Period Finding (Note)

We explored a **consistent** period‑finding approach tied to RCMO/EZA principles. The method is *not* more efficient than state‑of‑the‑art algorithms, but it reliably identifies co‑factors of semi‑primes and flags primes when factors are absent.

**Sketch (pseudocode):**
```
Given N:
  choose structured probe sequence S with weighted gates (EZA schedule)
  for each probe in S:
    compute modular residues; measure periodic signatures
    if stable periodicity emerges across gates:
       infer candidate factor(s) from period alignment
  if no candidates survive invariants:
       declare N likely prime (under this probe family)
```

This note is for historical context and reproducibility. Details and proofs are out of scope for this public repo.

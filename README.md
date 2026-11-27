# Main-Eigenvalue Switching for Families of Diameter-Five Trees

We construct sign switchings that make every distinct adjacency eigenvalue main for all uniform reflected diameter-five trees $T_r^p(a)$ ($r, a \ge 1$, $p \ge 0$), allowing arbitrary numbers of direct leaves at both centers. We also establish sufficient leaf-group size conditions for heterogeneous and nonreflected diameter-five trees, and derive exact algebraic constraints for the remaining diameter-five cases. The general diameter-five switching conjecture remains open outside the proved families.

[Paper PDF](paper/paper.pdf) · [LaTeX source](paper/paper.tex) · [Proof notes](switching/PROOF.md) · [Verification data](switching/EVIDENCE.md) · [Formal verification](FORMALIZATION.md) · [Prior work](PRIOR-WORK.md)

## Repository contents

- `paper/paper.tex`, `paper/paper.pdf` — full write-up of the theorems, proofs, and exact finite certificates.
- `switching/PROOF.md` — companion Markdown proof notes.
- `switching/CLAIM.md`, `switching/check_switching.py`, `switching/check_extensions.py` — frozen baseline claim and exact SymPy verification scripts (hashes recorded in `verification/FROZEN.sha256`).
- `switching/EVIDENCE.md` — summary of exact small-graph counts, resultant checks, and heterogeneous parameter rows.
- `verification/switching_controls.py` — independent cross-check of small-graph switching counts via rational primary spectral subspaces.
- `verification/check_lean_inputs.py` — cross-check of the 25 resultant polynomials embedded in Lean against symbolic SymPy computation.
- `formalization/FlipChoices.lean`, `formalization/ModularExclusions.lean` — Lean 4.34.1 formalization of the four-choice counting step and the 25 modular exclusion certificates.
- `replay.py` — end-to-end verification runner checking frozen SHA-256 hashes and executing all Python verification scripts.

## Reproducing the verification

### Exact Python/SymPy certificates

Requires Python 3.12 and SymPy 1.14.0 (`requirements.txt`):

```sh
python3 -m pip install -r requirements.txt
python3 -B replay.py
```

### Lean 4 formalization

Requires Lean 4.34.1 (`lean-toolchain`):

```sh
lean formalization/FlipChoices.lean
lean formalization/ModularExclusions.lean
```

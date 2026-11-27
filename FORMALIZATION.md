# Formal verification status

Lean 4.34.1 (toolchain specified in `lean-toolchain`) formally verifies two finite algebraic components of the proof with zero `sorry` and no custom axioms:

- [`formalization/FlipChoices.lean`](formalization/FlipChoices.lean): proves `Switching.four_choices`, the pigeonhole counting step showing that for any `a ≥ 5` and any three forbidden values `u, v, w : Nat`, there exists `k` with `1 ≤ k < a` distinct from `u, v, w`.
  - Axiom footprint: `[propext, Classical.choice, Quot.sound]`.
- [`formalization/ModularExclusions.lean`](formalization/ModularExclusions.lean): proves `Switching.eval_mod`, `Switching.no_integer_root`, `Switching.reflected_residues`, and `Switching.reflected_exclusions`, showing that all 25 reduced primitive resultant polynomials for $T_r^p(a)$ ($1 \le a, p \le 5$) have no integer roots via modular nonvanishing certificates.
  - Axiom footprint: `Switching.reflected_residues` uses no axioms; `Switching.no_integer_root` and `Switching.reflected_exclusions` use `[propext, Quot.sound]`.

## Commands

Run from the repository root with Lean 4.34.1:

```sh
lean formalization/FlipChoices.lean
lean formalization/ModularExclusions.lean
```

## Scope boundary

The script [`verification/check_lean_inputs.py`](verification/check_lean_inputs.py) (executed by `replay.py`) independently recomputes the 25 resultant polynomials over $\mathbb{Z}[r]$ from the radial model and checks that every coefficient list in `formalization/ModularExclusions.lean` matches identically. The spectral decomposition of diameter-five trees, the derivation of the radial resultant polynomials, and the verification that the constructed sign switchings detect every distinct eigenvalue are given as mathematical proofs in [`paper/paper.tex`](paper/paper.tex) and [`switching/PROOF.md`](switching/PROOF.md), supported by exact SymPy matrix and polynomial checks in `replay.py`.

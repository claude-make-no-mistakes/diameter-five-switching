# Formal verification status

Lean 4.34.1 checks [the four-choice lemma](formalization/FlipChoices.lean) used in the one-branch switching construction. It supplies an admissible leaf count whenever three eigenvalues can each forbid at most one count and there are at least four choices.

Run this command from the repository root with the toolchain specified in the toolchain file.

~~~sh
lean formalization/FlipChoices.lean
~~~

The paper proves the spectral decomposition, the overlaps, and the sufficiency conditions for the tree families. The Python certificate replays the finite exceptions and graph checks. Those steps remain outside Lean.

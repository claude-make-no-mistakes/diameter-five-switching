# Formal verification status

Lean 4.34.1 checks [the four-choice lemma](formalization/FlipChoices.lean) used in the one-branch switching construction. It supplies an admissible leaf count whenever three eigenvalues can each forbid at most one count and there are at least four choices.

Run this command from the repository root with the toolchain specified in the toolchain file.

~~~sh
lean formalization/FlipChoices.lean
lean formalization/ModularExclusions.lean
~~~

Lean also verifies the 25 modular residue certificates and proves that the represented polynomials have no integer root. The exact Python replay constructs the resultant polynomials from the radial model. The spectral decomposition, the identification of the resultants, and the proof that the constructed signs see every eigenvalue remain outside Lean.

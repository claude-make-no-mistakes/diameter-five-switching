# Exact verification

The frozen baseline inputs are verified against their SHA-256 digests (`verification/FROZEN.sha256`) before running the checks.

| Input | SHA-256 |
|---|---|
| `switching/CLAIM.md` | `c6f7a15459156af683baac8daac12dcfa380dd68d90112a1bf43cc481b94254e` |
| `switching/check_switching.py` | `90dbb7ad4ec3a074e0222f9e00e8a28d595f9e1ce210a35bf70379dafa9711c8` |
| `switching/check_extensions.py` | `14cf9c9c33733b142266a62d250044cb25c4219a7b49b7ce72231c164ce6b14c` |

## Replay

Run all checks from the repository root using Python 3.12 and SymPy 1.14.0:

```sh
python3 -B replay.py
```

This verifies the SHA-256 manifest and executes:

1. `switching/check_switching.py` — enumerates sign vectors modulo global negation on six small graphs, verifies the resultant congruence and eight divisor cases for $T_r(a)$, and verifies the constructed witness directly against the exact adjacency matrix spectrum for all 40 pairs $1 \le r \le 5$, $1 \le a \le 8$.
2. `switching/check_extensions.py` — enumerates four additional small graphs, computes the exact resultants $R_{a,p}(r) \in \mathbb{Z}[r]$ for all 25 pairs $1 \le a, p \le 5$ (confirming $(r, a, p) = (1, 2, 1)$ is the unique positive integer root), checks the exceptional witness on the adjacency matrix of $T_1^1(2)$, and finds exact witnesses for 180 heterogeneous parameter rows with one or two branches per side, branch sizes in $\{1, 2, 3\}$, and $p_i \in \{0, 1\}$. (Parameter rows can describe isomorphic trees because all four direct-leaf count pairs are included for each ordered pair of branch multisets.)
3. `verification/switching_controls.py` — independently reproduces the small-graph switching counts using irreducible factors of the minimal polynomial (rational primary spectral subspaces).
4. `verification/check_lean_inputs.py` — independently recomputes the 25 reduced primitive resultant polynomials and confirms exact coefficient-by-coefficient agreement with `formalization/ModularExclusions.lean`.

## Verified small-graph counts

Counts are given modulo global negation ($s \sim -s$):

| Graph | Successful sign classes |
|---|---:|
| $K_1$ | 1 |
| $K_2$ | 0 |
| $P_3$ | 2 |
| $P_4$ | 4 |
| $K_4 - e$ | 0 |
| $P_6$ | 24 |
| $K_{1,3}$ | 6 |
| $C_6$ | 12 |
| $K_{3,3}$ | 12 |
| Triangular prism | 12 |

The primary checkers work directly from exact integer adjacency matrices and compare the degree of the square-free characteristic polynomial with the exact Krylov rank. An independent check via multiplication-matrix determinants on $\mathbb{Q}[r][x]/(g)$ also reproduces all 25 resultants and modular certificates. The proofs in [`paper/paper.tex`](../paper/paper.tex) and [`switching/PROOF.md`](PROOF.md) supply the infinite quantifiers for $T_r(a)$, $T_r^p(a)$, and the sufficient leaf-group size bounds; the 180 parameter rows provide bounded exact evidence for the remaining diameter-five cases.

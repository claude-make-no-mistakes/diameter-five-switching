# Exact verification

The frozen inputs were hashed with SHA-256 before running the associated checks.

| Input | SHA-256 |
|---|---|
| `CLAIM.md` | `c6f7a15459156af683baac8daac12dcfa380dd68d90112a1bf43cc481b94254e` |
| `check_switching.py` | `90dbb7ad4ec3a074e0222f9e00e8a28d595f9e1ce210a35bf70379dafa9711c8` |
| `check_extensions.py` | `14cf9c9c33733b142266a62d250044cb25c4219a7b49b7ce72231c164ce6b14c` |

Replay from the repository root.

```sh
python -B switching/check_switching.py
python -B switching/check_extensions.py
```

Both checks exited with code 0 on Python 3.12.14 and SymPy 1.14.0. The first enumerated sign vectors modulo global negation on six graphs, verified the resultant congruence and divisor cases, then compared the constructed witness with the exact full adjacency spectrum for all 40 pairs \(1\le r\le5,1\le a\le8\).

The supplement enumerated four more known-answer graphs. For every \(1\le a,p\le5\), it computed the resultant for the proposed mirrored switch on \(T_r^p(a)\) as a polynomial of the unrestricted parameter \(r\). Its only positive integer root was \((r,a,p)=(1,2,1)\). The exceptional witness flips one branch leaf and one direct leaf on the same side. The supplement found exact witnesses for 180 parameter rows with one or two branches per side, branch sizes in \(\{1,2,3\}\), and zero or one direct leaf per side. The parameter rows can describe isomorphic trees. For each pair of branch multisets ordered according to the checker's list, all four direct-leaf count choices were included.

| Graph | Successful sign classes |
|---|---:|
| \(K_1\) | 1 |
| \(K_2\) | 0 |
| \(P_3\) | 2 |
| \(P_4\) | 4 |
| \(K_4-e\) | 0 |
| \(P_6\) | 24 |
| \(K_{1,3}\) | 6 |
| \(C_6\) | 12 |
| \(K_{3,3}\) | 12 |
| Triangular prism | 12 |

The checker works from the full integer adjacency matrix and compares the square-free characteristic polynomial degree with the exact Krylov rank. A separate arithmetic self-check reproduced the 25 modular certificates by taking the determinant of multiplication by \(h\) on \(\mathbb Q[r][x]/(g)\) in the basis \(1,x,x^2,x^3\). The proofs in `PROOF.md` supply the infinite quantifiers, including the reflected uniform family with direct leaves. The 180 parameter rows give bounded evidence for the unrestricted diameter-five problem.

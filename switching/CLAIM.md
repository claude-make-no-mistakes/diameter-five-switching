# Frozen claim and baseline

For every pair of integers \(r,a\geq 1\), let \(T_r(a)\) be the tree formed by joining two centers with one edge and attaching to each center \(r\) new branch vertices, each adjacent to \(a\) new leaves. There exists a sign vector \(s\in\{-1,1\}^{2+2r(a+1)}\) such that each distinct eigenspace of the ordinary adjacency matrix of \(T_r(a)\) has nonzero projection of \(s\). Equivalently, each distinct eigenvalue of the switched adjacency matrix \(\operatorname{diag}(s)A\operatorname{diag}(s)\) is main.

The first checker uses integer adjacency matrices and exact Krylov rank, compared with the exact square-free characteristic polynomial degree. The known-answer cases count successful sign vectors after identifying \(s\) with \(-s\). The frozen expectations are \(K_1:1\), \(K_2:0\), \(P_3:2\), \(P_4:4\), \(K_4-e:0\), and \(P_6:24\). The constructed signs must pass for all 40 pairs \(1\le r\le5,1\le a\le8\), including \(r=1,a=2\). The resultant and finite exceptional cases check the construction's arithmetic; the written argument supplies the infinite quantifier.

The broader question is whether the same existential statement holds for every tree of diameter five, including unequal branch sizes on either side and any number of leaves attached directly to either center. It is a separate target and is not assumed in the frozen baseline.

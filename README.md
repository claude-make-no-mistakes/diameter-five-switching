# Main-Eigenvalue Switching for Families of Diameter-Five Trees

We construct a sign switching that makes every distinct adjacency eigenvalue main for all uniform reflected diameter-five trees, allowing direct leaves at both centers. We also give sufficient size conditions for heterogeneous and nonreflected trees. The proof separates branch modes from the radial spectrum and uses exact arithmetic for the finite exceptions.

[Paper PDF](paper/paper.pdf) · [LaTeX source](paper/paper.tex) · [Proof notes](switching/PROOF.md) · [Verification data](switching/EVIDENCE.md)

## Replay the certificates

Use Python 3.12 and SymPy 1.14.0.

```sh
python -m pip install -r requirements.txt
python -B replay.py
```

The general conjecture remains open in this work. See [formal verification status](FORMALIZATION.md).

[Verification record](REVIEW.md) · [Draft post for X](POST.md)

"""Cross-check the Lean residue inputs against the radial resultant calculation."""

from ast import literal_eval
from pathlib import Path
import sys

from sympy import Poly, resultant

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "switching"))
from check_extensions import reflected_polynomials, r_parameter, x


def main():
    source = (ROOT / "formalization/ModularExclusions.lean").read_text(encoding="utf-8")
    table = source.split("def reflectedResultants :", 1)[1].split(":=", 1)[1].split("\n\n", 1)[0]
    entries = literal_eval(table.strip())
    if len(entries) != 25:
        raise ValueError("expected one residue certificate per (a,p) pair")
    for a in range(1, 6):
        for p in range(1, 6):
            radial, overlap = reflected_polynomials(r_parameter, a, p, 1, int(a == 1 and p >= 2))
            polynomial = Poly(resultant(radial, overlap, x), r_parameter).primitive()[1]
            if (a, p) == (2, 1):
                polynomial = polynomial.exquo(Poly(r_parameter - 1, r_parameter))
            elif (a, p) == (2, 2):
                polynomial = polynomial.exquo(Poly(r_parameter**2, r_parameter))
            modulus, coeffs = entries[(a - 1) * 5 + p - 1]
            if modulus <= 0 or coeffs != list(reversed(polynomial.all_coeffs())):
                raise ValueError(f"Lean coefficient mismatch for a={a}, p={p}")
    print("All 25 Lean polynomials match the independently recomputed resultants.")


if __name__ == "__main__":
    main()

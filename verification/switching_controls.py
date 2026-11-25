"""Check small sign counts using rational primary spectral subspaces."""

from itertools import combinations, product

from sympy import Matrix, eye, zeros


def sign_count(order, edges):
    adjacency = zeros(order)
    for i, j in edges:
        adjacency[i, j] = adjacency[j, i] = 1
    minimal = adjacency.charpoly().as_poly().sqf_part()
    detectors = []
    for factor, _ in minimal.factor_list()[1]:
        polynomial = minimal.exquo(factor)
        detector = zeros(order)
        for coeff in polynomial.all_coeffs():
            detector = adjacency * detector + coeff * eye(order)
        detectors.append(detector)
    good = 0
    for tail in product((-1, 1), repeat=order-1):
        signs = Matrix((1, *tail))
        # Rational signs make the visible spectrum a union of Galois orbits.
        if all(detector * signs != zeros(order, 1) for detector in detectors):
            good += 1
    return good, 2 ** (order-1)


def main():
    triangles = [(0, 1), (1, 2), (2, 0), (3, 4), (4, 5), (5, 3)]
    cases = [
        ("K2", 2, [(0, 1)], 0),
        ("K4-e", 4, list(combinations(range(4), 2))[1:], 0),
        ("K1,3", 4, [(0, j) for j in (1, 2, 3)], 6),
        ("P6", 6, [(i, i+1) for i in range(5)], 24),
        ("C6", 6, [(i, (i+1) % 6) for i in range(6)], 12),
        ("K3,3", 6, list(product(range(3), range(3, 6))), 12),
        ("prism", 6, triangles + [(i, i+3) for i in range(3)], 12),
    ]
    for name, order, edges, expected in cases:
        actual, total = sign_count(order, edges)
        if actual != expected:
            raise ValueError(f"{name}: got {actual}, expected {expected}")
        print(f"{name}: {actual}/{total}")


if __name__ == "__main__":
    main()

"""Exact baseline for all-eigenvalue main switching on symmetric depth-two trees."""

from itertools import combinations, product

from sympy import Matrix, Poly, resultant, symbols


x, r_symbol, a_symbol = symbols("x r a")


def graph(order, edges):
    neighbors = [[] for _ in range(order)]
    for left, right in edges:
        neighbors[left].append(right)
        neighbors[right].append(left)
    return neighbors


def path(order):
    return graph(order, ((vertex, vertex + 1) for vertex in range(order - 1)))


def diameter_five(sizes, direct_leaves=(0, 0)):
    edges = [(0, 1)]
    branches = [[], []]
    leaf_groups = [[], []]
    order = 2
    for center in (0, 1):
        for size in sizes[center]:
            branch = order
            leaves = tuple(range(order + 1, order + size + 1))
            edges.append((center, branch))
            edges.extend((branch, leaf) for leaf in leaves)
            branches[center].append((branch, leaves))
            order += size + 1
        for _ in range(direct_leaves[center]):
            edges.append((center, order))
            leaf_groups[center].append(order)
            order += 1
    return graph(order, edges), branches, leaf_groups


def distinct_spectrum_count(neighbors):
    adjacency = Matrix(
        len(neighbors), len(neighbors), lambda row, col: int(col in neighbors[row])
    )
    return adjacency.charpoly().as_poly().sqf_part().degree()


def has_full_main_spectrum(neighbors, signs, distinct_count):
    # For a real symmetric matrix, each visible eigenvalue contributes one
    # independent direction to span(s, As, ...), by Vandermonde interpolation.
    columns = []
    current = signs
    for _ in range(distinct_count):
        columns.append(current)
        current = [sum(current[index] for index in row) for row in neighbors]
    return Matrix(columns).rank() == distinct_count


def successful_switches(neighbors):
    spectrum_count = distinct_spectrum_count(neighbors)
    return sum(
        has_full_main_spectrum(neighbors, (1, *tail), spectrum_count)
        for tail in product((-1, 1), repeat=len(neighbors) - 1)
    )


def radial(e, r, a):
    return (x - e) * (x**2 - a) - r * x


def symmetric_signs(neighbors, branches, r, a):
    signs = [1] * len(neighbors)
    branch, leaves = branches[0][0]
    if (r, a) == (1, 2):
        signs[branch] = signs[leaves[0]] = -1
    else:
        f = Poly(radial(1, r, a), x)
        candidate_ks = range(1, min(4, max(1, a - 1)) + 1)
        k = next(
            k
            for k in candidate_ks
            if f.gcd(Poly(x**2 - a + r * x + r * a - k, x)).degree() == 0
        )
        for leaf in leaves[:k]:
            signs[leaf] = -1
    return signs


def check_arithmetic():
    f = radial(1, r_symbol, a_symbol)
    q = x**2 - a_symbol + r_symbol * x + r_symbol * a_symbol - 1
    assert resultant(f, q, x).subs(r_symbol, 0) == -a_symbol
    exceptional = []
    for a in range(1, 5):
        for r in range(1, a + 1):
            if a % r:
                continue
            f_num = Poly(radial(1, r, a), x)
            q_num = Poly(q.subs({r_symbol: r, a_symbol: a}), x)
            if f_num.gcd(q_num).degree() != 0:
                exceptional.append((r, a))
    assert exceptional == [(1, 2)], exceptional


def main():
    known_counts = {
        "K1": (path(1), 1),
        "K2": (path(2), 0),
        "P3": (path(3), 2),
        "P4": (path(4), 4),
        "K4-e": (graph(4, (edge for edge in combinations(range(4), 2) if edge != (0, 1))), 0),
        "P6": (path(6), 24),
    }
    for label, (neighbors, expected) in known_counts.items():
        actual = successful_switches(neighbors)
        assert actual == expected, (label, actual, expected)
        print(f"{label}: {actual} successful sign classes")
    check_arithmetic()
    print("Resultant congruence and exceptional divisor cases verified")

    verified = 0
    for r, a in product(range(1, 6), range(1, 9)):
        sizes = ((a,) * r,) * 2
        neighbors, branches, _ = diameter_five(sizes)
        spectrum_count = distinct_spectrum_count(neighbors)
        assert spectrum_count == 6 + (a >= 2) + 2 * (r >= 2), (r, a, spectrum_count)
        signs = symmetric_signs(neighbors, branches, r, a)
        assert has_full_main_spectrum(neighbors, signs, spectrum_count), (r, a)
        verified += 1
    print(f"T_r(a): {verified} constructed witnesses verified")


if __name__ == "__main__":
    main()

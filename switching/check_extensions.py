"""Exact tests for the reflected and unequal-branch extensions."""

from itertools import combinations_with_replacement, product

from sympy import Poly, resultant, symbols

from check_switching import (
    diameter_five,
    distinct_spectrum_count,
    graph,
    has_full_main_spectrum,
    successful_switches,
    x,
)


r_parameter = symbols("r")


def reflected_polynomials(r, a, p, branch_flips, direct_flips):
    branch_denominator = x**2 - a
    radial = (x - 1) * x * branch_denominator - r * x**2 - p * branch_denominator
    overlap = (
        (x**2 - r - p - 1) * x * branch_denominator
        - 2 * branch_flips * x
        - 2 * direct_flips * branch_denominator
    )
    return radial, overlap


def primary_resultants():
    """Return every positive integer r where the frozen primary pattern fails."""
    exceptions = []
    for a, p in product(range(1, 6), repeat=2):
        direct_flips = int(a == 1 and p >= 2)
        radial, overlap = reflected_polynomials(r_parameter, a, p, 1, direct_flips)
        obstruction = Poly(resultant(radial, overlap, x), r_parameter)
        assert not obstruction.is_zero, (a, p)
        positive_roots = sorted(root for root in obstruction.ground_roots() if root.is_Integer and root > 0)
        exceptions.extend((int(root), a, p) for root in positive_roots)
    return exceptions


def local_switches(branches, direct, center_signs=(1, 1)):
    """Search a bounded family with one altered leaf group per equal-size branch class."""
    sides = []
    for side in (0, 1):
        representatives = {}
        for branch, leaves in branches[side]:
            representatives.setdefault(len(leaves), (branch, leaves))

        groups = []
        for branch, leaves in representatives.values():
            groups.append(tuple(
                leaves[:k] + (branch,) * flip_branch
                for k, flip_branch in product(range(min(4, len(leaves)) + 1), (0, 1))
            ))
        if direct[side]:
            groups.append(tuple(tuple(direct[side][:k]) for k in range(min(4, len(direct[side])) + 1)))
        sides.append(tuple(product(*groups)))

    for left, right in product(*sides):
        minus = {vertex for group in (*left, *right) for vertex in group}
        minus.update(side for side in (0, 1) if center_signs[side] == -1)
        yield minus


def first_local_witness(sizes, leaf_counts):
    neighbors, branches, direct = diameter_five(sizes, leaf_counts)
    distinct_count = distinct_spectrum_count(neighbors)
    for center_signs in ((1, 1), (1, -1)):
        for minus in local_switches(branches, direct, center_signs):
            signs = [1 - 2 * (vertex in minus) for vertex in range(len(neighbors))]
            if has_full_main_spectrum(neighbors, signs, distinct_count):
                return tuple(sorted(minus))
    return None


def baseline_switch_counts():
    triangle = ((0, 1), (1, 2), (2, 0))
    prism_edges = (*triangle, *((a + 3, b + 3) for a, b in triangle), *((a, a + 3) for a in range(3)))
    baselines = {
        "K1,3": (graph(4, ((0, i) for i in range(1, 4))), 6),
        "C6": (graph(6, ((i, (i + 1) % 6) for i in range(6))), 12),
        "K3,3": (graph(6, product(range(3), range(3, 6))), 12),
        "prism": (graph(6, prism_edges), 12),
    }
    for name, (neighbors, expected) in baselines.items():
        actual = successful_switches(neighbors)
        assert actual == expected, (name, actual, expected)
        print(f"{name}: {actual} successful sign classes")


def main():
    baseline_switch_counts()
    exceptions = primary_resultants()
    print(f"Uniform reflected primary exceptions (r,a,p): {exceptions}")
    for r, a, p in exceptions:
        witness = first_local_witness(((a,) * r,) * 2, (p, p))
        assert witness is not None, (r, a, p)
        print(f"Uniform reflected exceptional witness for {(r, a, p)}: {witness}")

    lists = [(a,) for a in range(1, 4)] + list(combinations_with_replacement(range(1, 4), 2))
    checked = 0
    for left_index, left in enumerate(lists):
        for right in lists[left_index:]:
            for leaf_counts in ((0, 0), (0, 1), (1, 0), (1, 1)):
                witness = first_local_witness((left, right), leaf_counts)
                assert witness is not None, (left, right, leaf_counts)
                checked += 1
    print(f"Unequal-branch grid: {checked} exact witnesses verified")


if __name__ == "__main__":
    main()

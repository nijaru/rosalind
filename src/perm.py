from itertools import permutations


def print_perm(n):
    print(perm(n))
    [print(" ".join(([str(x) for x in p]))) for p in lperm(n)]


def perm(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return n * perm(n - 1)


def lperm(n):
    return [list(p) for p in permutations(range(1, n + 1))]


print_perm(7)

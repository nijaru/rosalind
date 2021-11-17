def fib(n, k, a=0, b=1):
    if n == 0:
        return 1
    if n == 1:
        return b
    return fib(n - 1, k, b * k, a + b)


print(fib(31, 2))

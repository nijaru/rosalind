def fibd(n, m):
    s = [1, 1]
    for i in range(2, n):
        if i < m:
            s.append(s[-2] + s[-1])
        elif i == n or i == n + 1:
            s.append(s[-2] + s[-1] - 1)
        else:
            s.append(s[-2] + s[-1] - s[-(m + 1)])


print(fibd(100, 17))

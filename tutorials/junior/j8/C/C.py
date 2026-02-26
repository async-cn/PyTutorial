def solve(n):
    s = 0
    for i in range(2, n+1):
        for j in range(1, i):
            s += i * j
    print(n, s)

solve(5)
solve(25)
solve(125)
solve(200)
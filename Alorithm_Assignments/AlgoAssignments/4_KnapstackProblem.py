def knapsack(W):
    items = [(i, i) for i in range(1, 11)]
    N = len(items)
    T = [[0 for j in range(W+1)] for i in range(N+1)]
    for i in range(1, N+1):
        for j in range(1, W+1):
            if items[i-1][1] > j:
                T[i][j] = T[i-1][j]
            else:
                T[i][j] = max(T[i-1][j], T[i-1][j-items[i-1][1]] + items[i-1][0])
    return T[N][W]

val = knapsack(8975000)
print(val)
# 실패

import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def dfs(x, y):
    if x < 0 or x >= m or y < 0 or y >= n:
        return False

    if graph[x][y] == 0:
        global cnt
        cnt += 1
        graph[x][y] = 1
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False


m, n, k = map(int, input().split()) # m행 n열
graph = [[0] * (n) for _ in range(m)]

for k in range(k):
    ly, lx, ry, rx = map(int, input().split())

    for i in range(lx, rx):
        for j in range(ly, ry):
            graph[i][j] = 1

result = 0
answer = []
for i in range(m):
    for j in range(n):
        cnt = 0
        if dfs(i, j):
            result += 1
            answer.append(cnt)

print(result)
answer.sort()
for i in answer:
    print(i, end=' ')

import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def dfs(x, y):
    if x <= -1 or x >= r or y <= -1 or y >= c:
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


r, c = map(int, input().split()) # r행 c열
graph = []
for _ in range(r):
    alpha = list(input().rstrip())
    for i in range(len(alpha)):
        alpha[i] = ord(alpha[i]) - 65
    graph.append(alpha)


# graph = [[0] * (c) for _ in range(r)]
#
# for k in range(k):
#     ly, lx, ry, rx = map(int, input().split())
#
#     for i in range(lx, rx):
#         for j in range(ly, ry):
#             graph[i][j] = 1
#
# result = 0
# answer = []
# for i in range(m):
#     for j in range(n):
#         cnt = 0
#         if dfs(i, j):
#             result += 1
#             answer.append(cnt)
#
# print(result)
# answer.sort()
# for i in answer:
#     print(i, end=' ')


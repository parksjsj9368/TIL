cnt = 0

def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    if graph[x][y] == 1:
        global cnt
        cnt += 1
        graph[x][y] = 0
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False


n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

result = 0
answer = []
for i in range(n):
    for j in range(n):
        cnt = 0
        if dfs(i, j) == True:
            result += 1
            answer.append(cnt)

print(result)
answer.sort()
for i in answer:
    print(i)
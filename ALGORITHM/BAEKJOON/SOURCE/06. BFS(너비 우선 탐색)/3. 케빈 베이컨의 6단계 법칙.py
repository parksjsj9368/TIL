from collections import deque

def bfs(v):

    count = 0
    q = deque([[v, count]])

    while q:
        value = q.popleft()
        v = value[0]
        count = value[1]

        if not visited[v]:
            visited[v] = True
            countList[v] += count
            count += 1

            for i in graph[v]:
                q.append([i, count])


n, m = map(int, input().split())

countList = [0] * (n+1)

graph = [[] for _ in range(n+1)]
for _ in range(m) :
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(1, n + 1):
    visited = [False] * (n + 1)
    bfs(i)

print(countList)
print(countList.index(min(countList[1:])))
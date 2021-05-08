# 함수
def dfs(graph, v, visited):
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# input
a = int(input())
b = int(input())

# graph
graph = [[] for _ in range(a+1)]
for i in range(b):
    c1, c2 = map(int, input().split())
    graph[c1].append(c2)
    graph[c2].append(c1)

# visited
visited = [False] * (a+1)

# result
dfs(graph, 1, visited)
print(sum(visited) - 1)
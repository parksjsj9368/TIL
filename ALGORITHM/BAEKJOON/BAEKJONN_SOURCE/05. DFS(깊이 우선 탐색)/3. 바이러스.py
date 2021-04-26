result = []

# 함수
def dfs(graph, v, visited):
    visited[v] = True
    result.append(v)

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

    return result


# input
data = []
a = int(input())
b = int(input())
for i in range(b):
    c = list(map(int, input().split()))
    data.append(c)

# graph
final = []
for i in range(len(data) + 2):
    results = []
    for j in range(len(data)):
        if (i in data[j]):
            results.append(data[j][0])
            results.append(data[j][1])
    final.append(list(set(results)))

graph = [[]]
for i in range(1, len(data) + 2):
    final[i].remove(i)
    graph.append(final[i])
# print(graph)


# visited
visited = [False] * 8

# result
a = dfs(graph, 1, visited)
# print(a)

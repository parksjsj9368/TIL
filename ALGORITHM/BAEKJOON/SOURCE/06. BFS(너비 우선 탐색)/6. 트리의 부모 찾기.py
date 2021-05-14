from collections import deque

n = int(input())
graph = [[] for _ in range(n+1)]
parents = [0] * (n+1)

for i in range(n-1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

queue=deque()
queue.append(1)

while queue:
    temp = queue.popleft()
    for i in graph[temp]:
        if parents[temp] != i:
            parents[i] = temp
            queue.append(i)

for i in parents[2:]:
    print(i)
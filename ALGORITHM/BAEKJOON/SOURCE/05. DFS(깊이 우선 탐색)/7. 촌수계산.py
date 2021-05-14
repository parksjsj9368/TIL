n = int(input()) # n:전체사람수
a, b = map(int, input().split()) # 촌수를 계산해야 하는 서로 다른 두 사람
m = int(input()) # m:부모자식들간의 관계수

adj = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split()) # x:y의부모, y:x의자녀
    adj[x].append(y)
    adj[y].append(x)

def dfs(vertex):
    global result

    if result > 0: # 결과값 나오면 종료
        return

    if vertex == b:  # a -> b 까지 도착
        # 촌수는 배열의 길이에서 -1 | ex) 나-아빠-할아버지 : 2촌
        result = visited.count(True) - 1
        return

    for neighbor in adj[vertex]:  # 현재노드와 인접한 노드 중에서
        if visited[neighbor] is False:  # 방문하지 않은 노드가 있으면
            visited[neighbor] = True  # 방문
            dfs(neighbor)  # 노드를 들고 다시 dfs
            visited[neighbor] = False  # 원하는 값에 도달하지 못하고 나오면 방문 목록에서 제거
    return

result = -1 # 기본값 : 촌수를 따질 수 없을 때 -1
visited = [False] * (n+1)
visited[a] = True # a 를 시작으로 두고
dfs(a)
print(result)

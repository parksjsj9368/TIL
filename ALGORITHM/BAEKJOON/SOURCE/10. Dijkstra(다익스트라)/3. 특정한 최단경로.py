import heapq
import sys
input = sys.stdin.readline
# 무한을 의미하는 값으로 10억을 설정
INF = int(1e9)

first = 1 #1번정점에서 n번정점으로의 최단거리
n, e = map(int, input().split())  # n:정점개수, e:간선개수


# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
graph = [[] for _ in range(n + 1)]

for _ in range(e):
    a, b, c = map(int, input().split())  # a에서 b 양방향 길이 c
    graph[a].append([b,c])
    graph[b].append([a,c])


v1, v2 = map(int, input().split())


def dijkstra(start) :
    # 최단 거리 테이블을 모두 무한으로 초기화
    distance = [INF] * (n + 1)
    q = []

    # 시작 노드로 가기 위한 최단 거리는 0으로 설정하여 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0

    # 큐가 비어있지 않다면
    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보를 꺼내기
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]

            # 현재 노드를 거쳐, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance


start_1 = dijkstra(first) #각 start기준에 따른 최단거리
start_v1 = dijkstra(v1)
start_v2 = dijkstra(v2)

answer = min(start_1[v1] + start_v1[v2] + start_v2[n], start_1[v2] +start_v2[v1] + start_v1[n])
if answer < INF : #위에 보면 값이 INF여도 계속 더하기에 조건을 ==이 아닌 <로 해주어야한다
    print(answer)
else :
    print(-1)
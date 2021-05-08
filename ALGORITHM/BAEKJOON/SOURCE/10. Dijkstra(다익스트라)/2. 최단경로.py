import heapq
import sys
input = sys.stdin.readline
# 무한을 의미하는 값으로 10억을 설정
INF = int(1e9)

V, e = map(int, input().split())  # V:정점개수, e:간선개수
k = int(input())  # k:정점시작번호(1~)


# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
graph = [[] for _ in range(V + 1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (V + 1)

for _ in range(e):
    u, v, w = map(int, input().split())  # u에서 v로 가는 가중치w
    graph[u].append([v, w])


def dijkstra(start) :
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

dijkstra(k)


for i in range(1, V+1):
    answer = distance[i]
    if answer == INF:
        print('INF')
    else :
        print(answer)

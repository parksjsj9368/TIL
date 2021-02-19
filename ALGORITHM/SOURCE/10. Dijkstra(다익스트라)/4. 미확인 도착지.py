import heapq
import sys
input = sys.stdin.readline
# 무한을 의미하는 값으로 10억을 설정
INF = int(1e9)


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



T = int(input()) # T:테스트케이스
for _ in range(T) :
    n, m, t = map(int, input().split()) # n:교차로개수, m:도로개수, t는 목적지후보개수
    s, g, h = map(int, input().split()) # s:출발지, g와 h 사이에 있는 도로를 지난다

    # 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
    graph = [[] for _ in range(n + 1)]

    for i in range(m) :
        a, b, d = map(int, input().split())  # a에서 b 양방향 길이 d
        graph[a].append([b,d])
        graph[b].append([a,d])

    t_list = []
    for j in range(t) :
        t_list.append(int(input()))


    start_s = dijkstra(s) #각 start기준에 따른 최단거리
    start_g = dijkstra(g)
    start_h = dijkstra(h)

    answer = []
    for k in t_list :
        if (start_s[g] + start_g[h] +start_h[k] == start_s[k]) or (start_s[h] + start_h[g] + start_g[k] == start_s[k]) :
            answer.append(k)
    answer.sort()
    for h in answer :
        print(h, end=' ')

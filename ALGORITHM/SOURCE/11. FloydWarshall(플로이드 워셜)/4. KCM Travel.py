# 무한을 의미하는 값 10억 설정
INF = int(1e9)

T = int(input())  # T:테스트케이스
for _ in range(T):
    n, m, k = map(int, input().split())  # n:공항수, m:총지원비용, k:티켓정보수

    graph = [[[INF, INF]] * (n + 1) for _ in range(n + 1)]
    # print(graph)
    # 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if a == b:
                graph[a][b] = [0, 0]

    for _ in range(k):
        u, v, c, d = map(int, input().split())  # u에서 v가는데 비용 c 소요시간 d
        if c <= m:
            graph[u][v] = [c, d]
    # print(graph)

    # 점화식에 따라 플로이드 워셜 알고리즘 수행
    for k in range(1, n + 1):  # 중간점
        for e in range(1, n + 1):  # 도착점

            if graph[1][k][0] + graph[k][e][0] <= m:
                if min(graph[1][e][1], graph[1][k][1] + graph[k][e][1]) != graph[1][e][1]:
                    graph[1][e][0] = graph[1][k][0] + graph[k][e][0]
                    graph[1][e][1] = graph[1][k][1] + graph[k][e][1]

    if graph[1][n][1] == INF:
        print('Poor KCM')
    else:
        print(graph[1][n][1])

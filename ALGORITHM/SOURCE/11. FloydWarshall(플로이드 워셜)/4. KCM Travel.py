# 무한을 의미하는 값 10억 설정
INF = int(1e9)

T = int(input())  # T:테스트케이스
for _ in range(T):
    n, m, k = map(int, input().split())  # n:공항수, m:총지원비용, k:티켓정보수


    graph = [[(INF,INF)] * (n+1) for _ in range(n+1)]
    # print(graph)

    for _ in range(k):
        u, v, c, d = map(int, input().split())  # u에서 v가는데 비용 c 소요시간 d
        if c <= m :
            graph[u][v] = c, d
    print(graph)

    #점화식에 따라 플로이드 워셜 알고리즘 수행
    for k in range(1, v+1) : # 중간점
        for b in range(1, v+1) : # 도착점

            if graph[1][k][0] + graph[k][b][0] > m :
                graph[1][b] = min(graph[1][b][1], INF)
            else :
                graph[1][b] = min(graph[1][b][1], graph[1][k][1] + graph[k][b][1])
    # print(graph)

    answer = INF
    for i in graph[1] :
        if type(i) == int :
            answer = min(answer, i)

    if answer == INF :
        print('POOR KCM')
    else :
        print(answer)

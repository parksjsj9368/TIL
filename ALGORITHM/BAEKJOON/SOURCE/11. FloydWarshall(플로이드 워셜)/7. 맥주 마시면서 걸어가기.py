INF = int(1e9)

t = int(input()) # t:테스트케이스


for _ in range(t) :
    INF = int(1e9)

    n = int(input()) # n:편의점개수


    array = []
    array.append(list(map(int, input().split())))  # 집 좌표 = 출발 좌표
    for _ in range(n) :
        array.append(list(map(int, input().split())))  # 편의점 좌표
    array.append(list(map(int, input().split())))  # 페스티벌 좌표


    # 2차원 리스트 만들고 무한으로 초기화
    graph = [[INF] * (n + 2) for _ in range(n + 2)]

    # 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
    # 거리마다 맥주 한박스(20개) 들고 출발, 50미터당 한병씩 마셔야되는데 가능하면 1로 !
    for a in range(n + 2) :
        for b in range(n + 2) :
            if a == b :
                graph[a][b] = 0
            else :
                diff = abs(array[a][0]-array[b][0]) + abs(array[a][1] - array[b][1])
                if diff <= 50 * 20 :
                    graph[a][b] = 1


    # 점화식에 따라 플로이드 워셜 알고리즘 수행
    for k in range(n + 2) :
        for a in range(n + 2) :
            for b in range(n + 2) :
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

    if graph[0][n+1] == INF :
        print('sad')
    else :
        print('happy')

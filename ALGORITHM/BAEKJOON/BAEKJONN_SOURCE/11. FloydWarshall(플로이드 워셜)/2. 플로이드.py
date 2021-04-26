# 무한을 의미하는 값 10억 설정
INF = int(1e9)

n = int(input()) # n:도시개수
m = int(input()) # m:버스개수


# 2차원 리스트 만들고 무한으로 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n+1) :
    for b in range(1, n+1) :
        if a == b :
            graph[a][b] = 0

for _ in range(m) :
    a, b, c = map(int, input().split()) # a에서 b까지 비용 c
    graph[a][b] = min(c, graph[a][b]) #노선이 하나가 아닐수도 있기에 최소값으로


# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n+1) : # 중간점
    for a in range(1, n+1) : # 시작점
        for b in range(1, n+1) : # 도착점
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과를 출력
for a in range(1, n+1) :
    for b in range(1, n+1) :
        if graph[a][b] == INF :
            print(0, end=' ')
        else :
            print(graph[a][b], end=' ')
    print()

# 무한을 의미하는 값 10억 설정
INF = int(1e9)

v, e = map(int, input().split()) # v:마을개수(1~), e:도로개수


# 2차원 리스트 만들고 무한으로 초기화
graph = [[INF] * (v+1) for _ in range(v+1)]

for _ in range(e) :
    a, b, c = map(int, input().split()) # a에서 b까지 거리 c
    graph[a][b] = c


# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, v+1) : # 중간점
    for a in range(1, v+1) : # 시작점
        for b in range(1, v+1) : # 도착점
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


answer = INF

for i in range(1, v+1) :
    answer = min(answer, graph[i][i])

if answer == INF :
    print(-1)
else :
    print(answer)

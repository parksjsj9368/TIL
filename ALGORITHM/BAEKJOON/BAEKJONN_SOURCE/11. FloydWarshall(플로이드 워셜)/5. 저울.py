# 무한을 의미하는 값 10억 설정
INF = int(1e9)

n = int(input()) # n:물건수
m = int(input()) # m:물건쌍수


graph = [[INF] * (n+1) for _ in range(n+1)]
# print(graph)

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b = map(int, input().split())  # a 무게 > b 무게
    graph[a][b] = 1 #1 표시가 나보다 작은얘 여부
# print(graph)


#점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n+1) : # 중간점
    for a in range(1, n+1) : # 시작점
        for b in range(1, n+1) : # 도착점
            if graph[a][k] + graph[k][b] == 2 :
                graph[a][b] = 1


cnt = [0] * (n+1)
#쌍방으로 관계를 아는 것 count
for a in range(1, n+1) :
    for b in range(1, n+1) :
        if graph[a][b] == 1:
            cnt[a] += 1
            cnt[b] += 1

# 비교 관계를 알 수 없는 ! 단 자기 관계 아니까 -1 ! 물건의 개수 출력
for i in cnt[1:] :
    print(n-i-1)
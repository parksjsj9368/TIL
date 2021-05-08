# 무한을 의미하는 값 10억 설정
INF = int(1e9)

n, m = map(int, input().split())  # n:학생수, m:비교횟수


graph = [[INF] * (n+1) for _ in range(n+1)]
# print(graph)

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b = map(int, input().split())  # a 학생 키 < b 학생 키
    graph[a][b] = 1 #1 표시가 나보다 키큰얘 여부
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

#모든 비교 관계를 알 수 있는 ! n-1 (자기자신 뺴고) 인 것이 몇 개 인가 ?!
print(cnt.count(n-1))
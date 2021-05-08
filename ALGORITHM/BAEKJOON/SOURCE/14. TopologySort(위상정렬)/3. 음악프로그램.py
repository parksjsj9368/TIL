from collections import deque

n, m = map(int, input().split()) # n:가수수(1~n), m:보조pd수
# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0 for _ in range(n + 1)]
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
graph = [[] for i in range(n + 1)]

# 방향 그래프의 모든 간선 정보를 입력 받기
for _ in range(m):
    data = list(map(int, input().split()))[1:]
    for i in range(len(data)-1) :
        graph[data[i]].append(data[i+1]) # i가 i+1앞에 서야한다
        # 진입 차수를 1 증가
        indegree[data[i+1]] += 1


# 위상 정렬 함수
def topology_sort():
    result = [] # 알고리즘 수행 결과를 담을 리스트
    q = deque() # 큐 기능을 위한 deque 라이브러리 사용

    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 원소 꺼내기
        now = q.popleft()
        result.append(now)
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)

    # 위상 정렬을 수행한 결과 출력
    if len(result) == n :
        for i in result:
            print(i)
    else :
        print(0)

topology_sort()

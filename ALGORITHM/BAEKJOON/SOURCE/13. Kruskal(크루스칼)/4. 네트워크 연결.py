import sys
input = sys.stdin.readline

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드를 찾을 때까지 재귀 호출
    if parent[x] == x:
        return x
    parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n = int(input()) # n:컴퓨터수
m = int(input()) # m:선의수

# 모든 간선을 담을 리스트와, 최종 비용을 담을 변수
edges = []
result = 0

parent = [i for i in range(n+1)] # 부모 테이블 초기화
for _ in range(m) :
    a, b, c = map(int, input().split()) # a 컴퓨터와 b 컴퓨터 연결 비용 c
    edges.append((c, a, b))

# 간선을 비용순으로 오름차순 정렬
edges.sort()

# 간선을 하나씩 확인
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
print(result)

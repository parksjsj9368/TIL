import sys
input = sys.stdin.readline

# 특정 원소가 속한 집합을 찾기
def find_parent(x):
    # 루트 노드를 찾을 때까지 재귀 호출
    if x == parent[x]:
        return x
    parent[x] = find_parent(parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m, k = map(int, input().split()) # n:학생수, m:친구관계수, k:가지고있는돈
cost = list(map(int, input().split())) # 각 학생이 원하는 친구비

# 부모 테이블상에서 부모를 자기 자신으로 초기화
parent = [i for i in range(n+1)]

for _ in range(m) :
    v, w = map(int, input().split())
    union_parent(v, w)

for i in range(1, len(parent)) :
    find_parent(i)


answer = {}
for i in range(1, len(parent)) :
    if parent[i] not in answer :
        answer[parent[i]] = cost[i-1]
    else :
        answer[parent[i]] = min(answer[parent[i]], cost[i-1])


if sum(answer.values()) <= k :
    print(sum(answer.values()))
else :
    print('Oh no')

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


n, m = map(int, input().split())  # n:점의개수(0~n-1), m:진행된차례의수
# 부모 테이블상에서 부모를 자기 자신으로 초기화
parent = [i for i in range(n+1)]
# 사이클 발생 여부
cycle = False


answer = 0
for i in range(m):
    a, b = map(int, input().split())

    # 사이클이 발생한 경우 종료
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        answer = i+1
        break

    else:
        # 사이클이 발생하지 않았다면 합집합(Union) 연산 수행
        union_parent(parent, a, b)

print(answer)

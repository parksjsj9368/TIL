import sys
sys.setrecursionlimit(10**5) # 런타임에러(recursionerror해결)
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


# 노드의 개수와 간선(Union 연산)의 개수 입력 받기
n, m = map(int, input().split())
# 부모 테이블상에서 부모를 자기 자신으로 초기화
parent = [i for i in range(n+1)]


for i in range(m):
    num, a, b = map(int, input().split())

    if num :
        if find_parent(a) == find_parent(b) :
            print('YES')
        else :
            print('NO')

    else :
        union_parent(a, b)

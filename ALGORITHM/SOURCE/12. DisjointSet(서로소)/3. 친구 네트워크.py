import sys
# sys.setrecursionlimit(10**5) # 런타임에러(recursionerror해결)
input = sys.stdin.readline

# 특정 원소가 속한 집합을 찾기
def find_parent(x):
    # 루트 노드를 찾을 때까지 재귀 호출
    if x == parent[x]:
        return x
    parent[x] = find_parent(parent[x])
    return parent[x]


# 두 원소가 속한 집합을 합치기
def union_parent(a, b, count):
    a = find_parent(a)
    b = find_parent(b)
    if a != b : # 숫자가 아닌 이름을 보고 합치기 하기에 변경
        parent[b] = a
        count[a] += count[b]


t = int(input()) # t:테스트케이스

for _ in range(t) :
    f = int(input()) # f:친구관계의수

    # 부모 테이블 초기화
    parent = {}
    count = {}

    for _ in range(f) :
        a, b = map(str, input().split())

        if a not in parent :
            parent[a] = a
            count[a] = 1
        if b not in parent :
            parent[b] = b
            count[b] = 1
        union_parent(a, b, count)
        print(count[find_parent(a)])
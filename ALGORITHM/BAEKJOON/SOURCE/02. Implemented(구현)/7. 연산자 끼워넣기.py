### 이해하기 어려운 문제

# 수의 개수
n = int(input())
# 수
a = list(map(int, input().split()))
# 덧셈, 뺼셈, 곱셈, 나눗셈 개수
add, sub, mul, div = map(int, input().split())

min_, max_ = 1e9, -1e9

def dfs(i, res, add, sub, mul, div):

    global max_, min_
    if i == n:
        max_ = max(res, max_)
        min_ = min(res, min_)
        return

    else:
        if add:
            dfs(i+1, res+a[i], add-1, sub, mul, div)
        if sub:
            dfs(i+1, res-a[i], add, sub-1, mul, div)
        if mul:
            dfs(i+1, res*a[i], add, sub, mul-1, div)
        if div:
            dfs(i+1, int(res/a[i]), add, sub, mul, div-1)

dfs(1, a[0], add, sub, mul, div)
print(max_)
print(min_)
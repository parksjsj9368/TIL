k, n = map(int, input().split())
k_list = []
for _ in range(k):
    k_list.append(int(input()))

start = 1
end = max(k_list)
result = 0

while start <= end:
    total = 0
    mid = (start + end) // 2

    for x in k_list:
        total += x // mid

    # 왼쪽 부분 탐색
    if total < n:
        end = mid - 1
    # 오른쪽 부분 탐색
    else:
        start = mid + 1
        result = mid

print(result)

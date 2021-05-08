n, m = map(int, input().split())
rope_list = list(map(int, input().split()))

start = 1
end = max(rope_list)
result = 0

while (start <= end):
    total = 0
    mid = (start + end) // 2

    for x in rope_list:
        if x > mid:
            total += x - mid

    if total < m:
        end = mid - 1

    else:
        result = mid
        start = mid + 1

print(result)
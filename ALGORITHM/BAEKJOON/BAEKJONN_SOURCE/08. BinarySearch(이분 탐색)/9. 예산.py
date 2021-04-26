n = int(input())
array = list(map(int, input().split()))
m = int(input())

start = 0
end = max(array)
result = 0

while start <= end:
    total = 0
    mid = (start + end) // 2

    for x in array:
        if x >= mid:
            total += mid
        else:
            total += x

    # 오른쪽 부분 탐색
    if total <= m:
        start = mid + 1
        result = mid
    # 왼쪽 부분 탐색
    else:
        end = mid - 1

print(result)

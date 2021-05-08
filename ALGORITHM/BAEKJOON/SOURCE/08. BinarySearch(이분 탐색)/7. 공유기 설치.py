# 이분탐색 응용문제

n, c = map(int, input().split())
array = []
for _ in range(n):
    array.append(int(input()))
array.sort()

start = 1
end = array[-1] - array[0] #최대거리
result = 0

while start <= end:
    mid = (start + end) // 2
    old = array[0] #배열 중 가장 낮은 좌표
    count = 1

    for i in range(1, len(array)) :
        if array[i] >= old+mid :
            count += 1
            old = array[i]

    # 왼쪽 부분 탐색
    if count < c:
        end = mid - 1
    # 오른쪽 부분 탐색
    else:
        start = mid + 1
        result = mid

print(result)
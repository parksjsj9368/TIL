from bisect import bisect_left, bisect_right

n = int(input())
check = list(map(int, input().split()))
check.sort()
m = int(input())
array = list(map(int, input().split()))


# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index

for i in array:
    answer = count_by_range(check, i, i)
    print(answer, end=' ')

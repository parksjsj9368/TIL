from bisect import bisect_left, bisect_right

n = int(input())
check = list(map(int, input().split()))
check.sort()

m = int(input())
array = list(map(int, input().split()))

def count_by_range(array, left_value, right_value) :
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index

for i in array :
    answer = count_by_range(check, i, i)

    if answer != 0 :
        answer = 1

    print(answer, end=' ')
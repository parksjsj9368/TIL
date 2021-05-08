# 퀵정렬
n = int(input())

data = []
for _ in range(n) :
    data.append(list(map(int, input().split())))

def quick_sort(array) :

    if len(array) <= 1 :
        return array

    pivot = array[0]
    tail = array[1:]

    left_side = [i for i in tail if i[1] < pivot[1]] \
                + [i for i in tail if i[1] == pivot[1] if i[0] < pivot[0]]
    right_side = [i for i in tail if i[1] > pivot[1]] \
                + [i for i in tail if i[1] == pivot[1] if i[0] > pivot[0]]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

answer = quick_sort(data)

for j in answer :
    print(j[0], j[1])


# 퀵정렬 알고리즘 아닌 코딩
#
# n = int(input())
#
# data = []
# for _ in range(n) :
#     data.append(list(map(int, input().split())))
#
# answer = sorted(data, key = lambda x : (x[1],x[0]))
#
# for j in answer:
#     print(j[0], j[1])
# 삽입정렬
n = int(input())
array = []
for _ in range(n) :
    array.append(int(input()))

for i in range(1, len(array)) :
    for j in range(i, 0, -1) :

        if array[j] < array[j-1] :
            array[j], array[j-1] = array[j-1], array[j]
        else :
            break

# 산술평균 : 수들의 합 / n, 소수점 이하 첫째 자리에서 반올림
print(int(round(sum(array)/len(array),0)))

# 중앙값 : 증가하는 순서로 중앙에 위치하는 값
print(array[len(array) // 2])

# 최빈값 : 가장 많이 나타나는 값, 여러개라면 두번째로 작은 값
x = {}
for b in array :
    if b in x :
        x[b] += 1
    else :
        x[b] = 1

y = [k for k, v in x.items() if v == max(sorted(x.values()))]
if len(y) == 1 :
    print(y[0])
else :
    print(y[1])

# 범위 : 최대값과 최소값의 차이
print(max(array) - min(array))


# 삽입정렬 알고리즘 아닌 코딩
#
# n = int(input())
# array = []
# for _ in range(n) :
#     array.append(int(input()))
# array.sort()
#
# # 산술평균 : 수들의 합 / n, 소수점 이하 첫째 자리에서 반올림
# print(int(round(sum(array)/len(array),0)))
#
# # 중앙값 : 증가하는 순서로 중앙에 위치하는 값
# print(array[len(array) // 2])
#
# # 최빈값 : 가장 많이 나타나는 값, 여러개라면 두번째로 작은 값
# x = {}
# for b in array :
#     if b in x :
#         x[b] += 1
#     else :
#         x[b] = 1
#
# y = [k for k, v in x.items() if v == max(sorted(x.values()))]
# if len(y) == 1 :
#     print(y[0])
# else :
#     print(y[1])
#
# # 범위 : 최대값과 최소값의 차이
# print(max(array) - min(array))
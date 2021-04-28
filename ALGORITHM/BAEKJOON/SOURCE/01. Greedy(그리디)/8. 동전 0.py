n, k = map(int, input().split())
cost = []
for _ in range(n) :
    cost.append(int(input()))

cost.sort(reverse=True)
count = 0

for i in cost :

    if i <= k :
        count += k // i
        k = k % i

    if k == 0 :
        break

print(count)


# 숏 코딩
#
# n, k = map(int, input().split())
# cost = []
# for _ in range(n) :
#     cost.append(int(input()))
#
# count = 0
#
# for i in array[::-1] :
#     count += k // i
#     k %= i
# print(count)
n = int(input())
p = list(map(int, input().split()))
p.sort()

tol = 0
list = []

for i in p :
    tol += i
    list.append(tol)
print(sum(list))


# 숏 코딩
#
# n = int(input())
# p = list(map(int, input().split()))
# p.sort()
#
# result = 0
#
# for i in range(n) :
#     result += sum(p[0:i+1])
# print(result)

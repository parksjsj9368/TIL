# 삽입정렬
n = list(map(int, input()))

for i in range(1, len(n)) :
    for j in range(i, 0, -1) :

        if n[j] > n[j-1] :
            n[j], n[j-1] = n[j-1], n[j]
        else :
            break

for j in n :
    print(j, end='')


# 삽입정렬 알고리즘 아닌 코딩
#
# n = list(map(int, input()))
# n.sort(reverse=True)
#
# for j in n:
#     print(j, end='')
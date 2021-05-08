# 2 : 2 4 8 6 ...
# 3 : 3 6 9 1 ...
# 4 : 4 6 ...
# 7 : 7 9 3 1 ...
# 8 : 8 4 2 6 ...
# 9 : 9 1 ...

T = int(input())
for _ in range(T):
    a, b = map(int, input().split()) # 문제 : a의b승 맨 뒷자리
    a = int(str(a)[-1])

    if a == 0: # 0은 10으로
        print(10)
        continue
    elif (a == 1) | (a == 5) | (a == 6):
        print(a)
        continue

    lst = []
    x = 1
    for _ in range(b):
        x *= a
        x %= 10

        if x in lst:
            break
        else:
            lst.append(x)

    answer = lst[b % len(lst) - 1]
    print(answer)
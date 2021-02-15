t = int(input())
for _ in range(t) :
    n = int(input())
    l = sorted(list(map(int, input().split())))

    odd = []
    even = []

    for i in range(n) :
        if i % 2 == 0 :
            odd.append(l[i])
        else :
            even.append(l[i])
    even.reverse()
    total = odd+even

    result = 0
    for j in range(n-1) :
        diff = abs(total[j+1] - total[j])
        result = max(diff, result)

    print(result)
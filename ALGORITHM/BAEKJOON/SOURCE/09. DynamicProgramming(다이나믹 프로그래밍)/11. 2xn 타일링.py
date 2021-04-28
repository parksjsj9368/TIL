n = int(input())

array=[0] * (n+1)
for i in range(1,n+1):
    if i == 1:
        array[i] = 1
        continue
    elif i == 2:
        array[i] = 2
        continue

    array[i] = array[i-1] + array[i-2]

print( array[n] % 10007 )
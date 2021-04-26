numbers = [1,1,1,1,1]
target = 3

a = [0]

for i in numbers:
    b = []
    for j in a:
        b.append(j+i)
        b.append(j-i)
    a=b

print(a.count(target))

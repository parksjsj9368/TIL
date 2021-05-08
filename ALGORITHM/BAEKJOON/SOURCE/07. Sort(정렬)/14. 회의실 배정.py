n = int(input())

data = []
for _ in range(n) :
    data.append(list(map(int, input().split())))

data = sorted(data, key=lambda item: item[0])
data = sorted(data, key=lambda item: item[1])

end = data[0][1]
d = 1

for i in range(1, len(data)):
    start = data[i][0]
    finish = data[i][1]

    if end <= start:
        end = finish
        d += 1

print(d)
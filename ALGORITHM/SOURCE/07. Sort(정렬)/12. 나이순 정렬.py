n = int(input())

data = []
for _ in range(n) :
    data.append(list(input().split()))

answer = sorted(data, key = lambda x : int(x[0]))

for x, y in answer :
    print(x, y)
n = int(input())

data = []
for _ in range(n) :
    data.append(int(input()))
data.sort(reverse=True)

answer = []
answer.append(data[0])

for i in range(1, len(data)) :
    answer.append(data[i] * (i+1))

print(max(answer))

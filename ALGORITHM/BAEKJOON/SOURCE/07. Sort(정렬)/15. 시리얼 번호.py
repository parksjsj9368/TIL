n = int(input())

data = []
for _ in range(n) :
    data.append(list(input()))

def data_sum(x) :
    sum = 0
    for i in x :
        if i.isnumeric() :
            sum += int(i)
    return sum

answer = sorted(data, key = lambda x : (len(x), data_sum(x), x))

for i in range(len(answer)) :
    print(''.join(answer[i]))
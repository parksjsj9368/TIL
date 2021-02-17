n = int(input())
cost = []
for _ in range(n) :
    cost.append(list(map(int, input().split())))

for i in range(1, n) :
    # 빨강으로 칠했을때
    cost[i][0] = min(cost[i-1][1], cost[i-1][2]) + cost[i][0]
    # 초록으로 칠했을때
    cost[i][1] = min(cost[i - 1][0], cost[i - 1][2]) + cost[i][1]
    # 파랑으로 칠했을때
    cost[i][2] = min(cost[i - 1][0], cost[i - 1][1]) + cost[i][2]

print(min(cost[n-1]))


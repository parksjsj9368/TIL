import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # n:수개수, m:합구해야하는횟수
num = list(map(int, input().split()))

# 접두사 합(Prefix Sum) 배열 계산
sum_value = 0
prefix_sum = [0]
for i in num:
    sum_value += i
    prefix_sum.append(sum_value)

for _ in range(m) :
    i, j = map(int, input().split()) # 합을 구해야하는 구간 i와 j
    print(prefix_sum[j] - prefix_sum[i-1])

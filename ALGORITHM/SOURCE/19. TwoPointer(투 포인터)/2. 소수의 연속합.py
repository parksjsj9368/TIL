import math

n = int(input())
array = [True for i in range(n + 1)] # 처음엔 모든 수가 소수(True)인 것으로 초기화

# 에라토스테네스의 체 알고리즘
for i in range(2, int(math.sqrt(n)) + 1): # 2부터 n의 제곱근까지의 모든 수를 확인하며
    if array[i] == True: # i가 소수인 경우 (남은 수인 경우)
        # i를 제외한 i의 모든 배수를 지우기
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1


sosu = []
for i in range(2, n + 1):
    if array[i]:
        sosu.append(i)


count = 0
interval_sum = 0
end = 0

for start in range(len(sosu)):
    while interval_sum < n and end < len(sosu):
        interval_sum += sosu[end]
        end += 1

    if interval_sum == n :
        count += 1
    interval_sum -= sosu[start]
print(count)
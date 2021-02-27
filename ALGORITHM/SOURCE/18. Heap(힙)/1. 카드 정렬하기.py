import sys
input = sys.stdin.readline

import heapq

n = int(input())
num = []
for _ in range(n) :
    num.append(int(input()))

if n == 1 :
    print(0)

else :
    heapq.heapify(num)
    answer = 0

    while len(num) > 1:
        a = heapq.heappop(num)
        b = heapq.heappop(num)
        heapq.heappush(num, a+b)
        answer += (a+b)
    print(answer)
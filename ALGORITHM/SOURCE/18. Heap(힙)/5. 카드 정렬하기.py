import sys
input = sys.stdin.readline

import heapq

n = int(input())
nums = []
for _ in range(n) :
    nums.append(int(input()))

if n == 1 :
    print(0)

else :
    heapq.heapify(nums)
    answer = 0

    while len(nums) > 1:
        a = heapq.heappop(nums)
        b = heapq.heappop(nums)
        heapq.heappush(nums, a+b)
        answer += (a+b)
    print(answer)
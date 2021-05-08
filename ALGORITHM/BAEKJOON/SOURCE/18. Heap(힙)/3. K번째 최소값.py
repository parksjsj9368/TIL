import heapq

def kth_smallest(nums, k) :
    heap = []
    for num in nums :
        heapq.heappush(heap, num) # (우선순위, 값)

    for _ in range(k) :
        kth_min = heapq.heappop(heap)
    return kth_min

print(kth_smallest([4, 1, 7, 3, 8, 5], 3))
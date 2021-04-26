import sys, heapq
input = sys.stdin.readline

n = int(input())
graph = []
for i in range(n):
    for j in list(map(int, input().split())):
        heapq.heappush(graph, j)
        if len(graph) > n:
            heapq.heappop(graph)
print(graph[0])

# 메모리 초과
#
# n = int(input())
# num_list = []
# for i in range(n):
#     num_list.extend(map(int, input().split()))
#
# num_sort = sorted(num_list, reverse=True)
# print(num_sort[n-1])

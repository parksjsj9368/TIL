n, k = map(int, input().split())

from collections import deque
queue = deque(i for i in range(1, n+1))
result = []

while len(queue) > 1 :
    for _ in range(k-1) :
        queue.append(queue.popleft())
    result.append(str(queue.popleft()))

print("<%s>" %(', '.join(result)))

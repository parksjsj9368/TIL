from collections import deque

n = int(input())
queue = deque(enumerate(map(int, input().split())))
answer = []

while 1:
    index, num = queue.popleft()
    answer.append(index+1)

    if not queue:
        break

    if num > 0:
        queue.rotate(-(num - 1))
    elif num < 0:
        queue.rotate(-num)

print(' '.join(map(str, answer)))

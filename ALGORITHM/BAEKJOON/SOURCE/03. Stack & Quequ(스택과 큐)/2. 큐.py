import sys
input = sys.stdin.readline

n = int(input())
from collections import deque
queue = deque()

for _ in range(n) :
    play = input().split()

    # push : 큐 넣기
    if play[0] == 'push' :
        queue.append(play[1])

    # pop : 가장 앞 정수 빼고, 그 수 출력. 정수 없는 경우 -1 출력
    if play[0] == 'pop' :
        if len(queue) != 0 :
            print(queue.popleft())
        else :
            print(-1)

    # size : 정수 개수 출력
    elif play[0] == 'size' :
        print(len(queue))

    # empty : 큐 비어있으면 1, 아니면 0 출력
    elif play[0] == 'empty' :
        if len(queue) == 0 :
            print(1)
        else :
            print(0)

    # front : 가장 앞 정수 출력. 정수 없는 경우 -1 출력
    elif play[0] == 'front' :
        if len(queue) != 0 :
            print(queue[0])
        else :
            print(-1)

    # back : 가장 뒤 정수 출력. 정수 없는 경우 -1 출력
    elif play[0] == 'back' :
        if len(queue) != 0 :
            print(queue[-1])
        else :
            print(-1)

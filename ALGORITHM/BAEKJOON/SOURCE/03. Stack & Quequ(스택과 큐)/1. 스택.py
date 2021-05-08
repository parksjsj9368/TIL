import sys
input = sys.stdin.readline

n = int(input())
stack = []

for _ in range(n) :
    play = input().split()

    # push x : 스택 넣기
    if play[0] == 'push' :
        stack.append(play[1])

    # pop : 가장 위 정수 빼고, 그 수 출력. 정수 없는 경우 -1 출력
    elif play[0] == 'pop' :
        if len(stack) != 0 :
             print(stack.pop())
        else :
            print(-1)

    # size : 정수 개수 출력
    elif play[0] == 'size' :
        print(len(stack))

    # empty : 스택 비어있으면 1, 아니면 0 출력
    elif play[0] == 'empty' :
        if len(stack) == 0 :
            print(1)
        else :
            print(0)

    # top : 가장 위 정수 출력. 정수 없는 경우 -1 출력
    elif play[0] == 'top' :
        if len(stack) != 0 :
            print(stack[-1])
        else :
            print(-1)

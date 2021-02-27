import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # n:표의크기, m:합구해야하는횟수

array = [[] for _ in range(n)]

for i in range(n) :
    array[i] = list(map(int, input().split()))

for _ in range(m) :
    x1, y1, x2, y2 = map(int, input().split())
    answer = 0

    for i in range(x1-1, x2) :
        for j in range(y1-1, y2) :
            answer += array[i][j]
    print(answer)

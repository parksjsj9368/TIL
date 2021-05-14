import sys
input = sys.stdin.readline

r, c = map(int, input().split()) # r:세로칸, c:가로칸
board = [list(map(lambda x : ord(x)-65, input().strip())) for _ in range(r)]
alpha = [0] * 26

# 좌, 하, 우, 상
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def dfs(x, y, m):
    global answer
    answer = max(m, answer)

    # 좌우상하 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # index 벗어나지 않는지 체크하고, 새로운 칸이 중복되는 알파벳인지 체크한다
        if (0 <= nx < r) and (0 <= ny < c) and (alpha[board[nx][ny]] == 0):
            alpha[board[nx][ny]] = 1
            dfs(nx, ny, m+1)
            alpha[board[nx][ny]] = 0 # 백트래킹

answer = 1
alpha[board[0][0]] = 1
dfs(0, 0, answer)
print(answer)

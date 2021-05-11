import sys

# 좌, 하, 우, 상
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def dfs(x, y, ans):
    global answer
    answer = max(ans, answer)

    # 좌우상하 다 확인한다
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # index 벗어나지 않는지 체크하고, 새로운 칸이 중복되는 알파벳인지 체크한다
        if ((0 <= nx < R) and (0 <= ny < C)) and (board[nx][ny] not in passed):
            passed.append(board[nx][ny])
            dfs(nx, ny, ans+1)
            passed.remove(board[nx][ny]) # 백트래킹

R, C = map(int, input().split())
board = [list(input().strip()) for _ in range(R)]

answer = 1
dfs(0, 0, answer)
print(answer)
def blocks(m, n, board):
    visited = set()

    # 2*2 되는 얘들 visited 집합에 추가하기
    for i in range(1, n):
        for j in range(1, m):
            if board[i][j] == board[i - 1][j - 1] == board[i - 1][j] == board[i][j - 1] != '_':
                visited.update([(i, j), (i - 1, j - 1), (i - 1, j), (i, j - 1)])

    # 2*2 되는 얘들 1로 표시
    for a, b in visited:
        board[a][b] = 1

    # 1인 애들 수만큼 '_'로 대체해 맨 앞으로 옮긴다
    for row, value in enumerate(board):
        tmp = ['_'] * value.count(1)
        board[row] = tmp + [b for b in value if b != 1]
    return len(visited)


def solution(m, n, board):
    answer = 0
    board = list(map(list, zip(*board))) # 행과열 변환

    while True:
        result = blocks(m, n, board)
        if result == 0:
            return answer
        answer += result
    return answer

print(solution(6,6,["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))

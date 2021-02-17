n = str(input())
x, y = int(n[1]), ord(n[0])

# ord() : 문자열을 아스키코드로 반환할 수 있는 함수
# print(ord('a'))
# print(ord('z'))

# 평2수1 평2수-1 평-2수1 평-2수-1 직2평1 직2평-1 직-2평1 직-2평-1
dx = [1,-1,1,-1, 2,2,-2,-2]
dy = [2,2,-2,-2, 1,-1,1,-1]
count = 0

for i in range(8) :
    nx = x + dx[i]
    ny = y + dy[i]

    if (nx < 1) or (ny < 97) or (nx > 8) or (ny > 122):
        continue
    count += 1

print(count)


# 동빈나씨 코드
#
# input_data = input()
# row = int(input_data[1])
# column = int(ord(input_data[0])) - int(ord('a')) + 1
#
# # 나이트가 이동할 수 있는 8가지 방향 정의
# steps = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]
#
# result = 0
#
# # 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
# for step in steps:
#
#     # 이동하고자 하는 위치 확인
#     next_row = row + step[0]
#     next_column = column + step[1]
#
#     # 해당 위치로 이동이 가능하다면 카운트 증가
#     if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
#         result += 1
#
# print(result)
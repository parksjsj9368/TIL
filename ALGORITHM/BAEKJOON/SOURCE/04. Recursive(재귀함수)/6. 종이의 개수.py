# 재귀함수

import sys
input = sys.stdin.readline

def check_paper(width, x, y):
	point = arr[x][y]
	for i in range(x, x + width):
		for j in range(y, y + width):
			if point != arr[i][j]:
				return [False, -1]
	return [True, point]

def make_paper(width, x, y):
	check = check_paper(width, x, y)

	if check[0]:
		count[check[1]] += 1
		return
	else:
		for i in range(3):
			for j in range(3):
				make_paper(width // 3, x + i * width // 3, y + j * width // 3)

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
count = {-1: 0, 0: 0, 1: 0}

make_paper(n, 0, 0)
for cnt in count.values():
	print(cnt)

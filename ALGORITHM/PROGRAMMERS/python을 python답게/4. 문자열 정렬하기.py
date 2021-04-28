## 문자열 s와 자연수 n이 입력으로 주어집니다.
## 문자열 s를 좌측 / 가운데 / 우측 정렬한 길이 n인 문자열을 한 줄씩 프린트해보세요.

s, n = input().strip().split(' ')
print(s.ljust(int(n)))
print(s.center(int(n)))
print(s.rjust(int(n)))


# 왼쪽 정렬 : str.ljust(size)
# 가운데 정렬 : str.center(size)
# 오른쪽 정렬 : str.rjust(size)

# str.rjust(size, '*') : str을 오른쪽 정렬하되 공간을 '*'로 채운다
# str.zfill(3) : str을 오른쪽 정렬하되 공간을 0으로 채운다

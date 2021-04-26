n, m = map(int, input().split())

# 모든 순열 구하기 (중복 허용)
from itertools import product
result = list(product(range(1,n+1), repeat=m))
# print(result)

for i in result :
    print(*i)
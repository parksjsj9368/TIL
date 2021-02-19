# 소수 판별 함수 : 개선된 알고리즘
import math

def is_prime_number(x) :
	for i in range(2, int(math.sqrt(x)) + 1) :
		if x % i == 0 :
			return False
		return True


# # 소수 판별 함수 (2이상의 자연수에 대하여)
# def is_prime_number(x) :
#     # 2부터 (x-1)까지의 모든 수를 확인하며
#     for i in range(2, x) :
#         # x가 해당 수로 나누어 떨어진다면
#         if x % i == 0:
#             # 소수가 아니다
#             return False
#         # 소수이다
#         return True
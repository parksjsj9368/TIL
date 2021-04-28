## base 진법으로 표기된 숫자를 10진법 숫자 출력해보세요.

num, base = map(int, input().strip().split(' '))
# int(str(x), base=n) : n진수를 10진수로 변환
print(int(str(num), base))


# # n진수 => 10진수
# int(str(x), base=n)
# # 10진수 => 2진수, 8진수, 16진수
# 2진수 : bin(x)[2:]
# 8진수 : oct(10)[2:]
# 10진수 : hex(10)[2:]
# # n진수 => n진수
# def convert(num, base) :
#     q, r = divmod(num, base)
#     if q == 0 :
#         return tmp[r]
#     else :
#         return convert(q, base) + tmp[r]

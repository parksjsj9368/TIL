n = int(input())

def fibo(n) :
    if n == 0 :
        answer = 0
    elif n == 1 :
        answer = 1
    else :
        answer = fibo(n-1) + fibo(n-2)
    return answer

print(fibo(n))


#재귀함수 알고리즘이 아닌 코딩
#
# n = int(input())
#
# a1 = 0
# a2 = 1
#
# if n == 0 :
#     print(a1)
# elif n == 1 :
#     print(a2)
# else :
#     for _ in range(n-1) :
#         a2, a1 = a1+a2, a2
#     print(a2)
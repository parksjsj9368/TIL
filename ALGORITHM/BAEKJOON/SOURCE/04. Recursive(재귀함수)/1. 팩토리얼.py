n = int(input())
answer = 0

def factorial_recursive(n) :
    if n <= 1 :
        answer = 1
    else :
        answer = n * factorial_recursive(n-1)
    return answer

print(factorial_recursive(n))


# 재귀함수 알고리즘이 아닌 코딩
#
# n = int(input())
# answer = 1
#
# for i in range(1, n+1) :
#     answer *= i
#
# print(answer)

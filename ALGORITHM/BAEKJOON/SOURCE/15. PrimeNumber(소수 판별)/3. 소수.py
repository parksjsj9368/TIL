import math

def is_prime_number(x) :
    if x == 1 :
        return False
    else :
        for i in range(2, int(math.sqrt(x)) + 1) :
            if x % i == 0 :
                return False
        return True


m = int(input())
n = int(input())

result = []
for i in range(m, n+1) :
    if is_prime_number(i) == True :
        result.append(i)

if len(result) == 0 :
    print(-1)
else :
    print(sum(result))
    print(min(result))

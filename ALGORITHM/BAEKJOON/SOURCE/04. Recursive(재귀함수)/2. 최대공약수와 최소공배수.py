a, b = map(int, input().split())

# 최대공약수
def gcd(a,b) :
    if a % b == 0 :
        return b
    else :
        return gcd(b, a%b)

# 최소공배수
def lcm(a,b) :
    x = a // gcd(a,b)
    y = b // gcd(a,b)
    return x*y*gcd(a,b)

print(gcd(a,b), lcm(a,b), sep='\n')

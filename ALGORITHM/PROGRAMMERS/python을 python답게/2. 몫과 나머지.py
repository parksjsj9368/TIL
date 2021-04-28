## 숫자 a, b가 주어졌을 때 a를 b로 나눈 몫과 a를 b로 나눈 나머지를 공백으로 구분해 출력해보세요.

# a, b = map(int, input().strip().split(' '))
# print(a//b, a%b)


# 큰 수를 다룰 때는 divmod를 사용하는게 좋다
# divmod(복소수, 복소수) => (몫, 나머지) 출력된다
a, b = map(int, input().strip().split(' '))
print(*divmod(a,b))

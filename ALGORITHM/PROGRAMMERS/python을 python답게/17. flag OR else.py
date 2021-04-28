## 본 문제에서는 자연수 5개가 주어집니다.
## 1. 숫자를 차례로 곱해 나온 수가 제곱수1가 되면 found를 출력하고
## 2. 모든 수를 곱해도 제곱수가 나오지 않았다면 not found를 출력하는 코드를 작성해주세요.

a = [int(input()) for _ in range(5)]
num = 1
answer = 'not found'
for i in a:
    num *= i
    if num ** (1/2) == int(num ** (1/2)):
        answer = 'found'
        break
print(answer)


a = [int(input()) for _ in range(5)]
num = 1
for i in a:
    num *= i
    if num ** (1/2) == int(num ** (1/2)):
        print('found')
        break
else:
    print('not found')

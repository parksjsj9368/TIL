## 입력으로 0이 주어지면 영문 소문자 알파벳을,
## 입력으로 1이 주어지면 영문 대문자 알파벳을 사전 순으로 출력하는 코드를 짜세요.

for i in range(ord('a'), ord('z')+1):
    print(chr(i), end='')
for i in range(ord('A'), ord('Z')+1):
    print(chr(i), end='')


import string
string.ascii_lowercase #소문자
string.ascii_uppercase #대문자
string.ascii_letters #대소문자 모두

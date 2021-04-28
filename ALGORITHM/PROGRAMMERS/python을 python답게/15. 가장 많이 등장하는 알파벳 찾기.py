## 이 문제에는 표준 입력으로 문자열, mystr이 주어집니다.
## mystr에서 가장 많이 등장하는 알파벳만을 사전 순으로 출력하는 코드를 작성해주세요.

import collections

my_str = input().strip()

count = collections.Counter(sorted(my_str))
max_value = max(list(count.values()))

answer = ''
for key in list(count.keys()):
    if count[key] == max_value:
        answer += key
print(answer)

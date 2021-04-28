## 문자열을 담은 이차원 리스트, mylist 가 solution 함수의 파라미터로 주어집니다.
## solution 함수가 mylist를 일차원 리스트로 만들어 리턴하도록 코드를 작성해주세요.

mylist = [[1, 2], [3, 4], [5, 6]]

# 리스트 컴프리헨션
[y for x in mylist for y in x]

# itertools.chain
import itertools
list(itertools.chain.from_iterable(mylist))

# itertools.unpacking
import itertools
list(itertools.chain(*mylist))

# sum 함수
answer = sum(mylist, [])

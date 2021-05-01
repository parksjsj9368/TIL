## 숫자를 담은 일차원 리스트, mylist에 대해
## mylist의 원소로 이루어진 모든 순열을 사전순으로 리턴하는 함수 solution을 완성해주세요.

import itertools

def solution(mylist):
    mylist = sorted(mylist)
    answer = list(map(list, itertools.permutations(mylist)))
    return answer


# 순열 : itertools.permutations
# 조합 : itertools.combinations

# itertools.permutations(list, n) : n개의 원소로 수열 만들기

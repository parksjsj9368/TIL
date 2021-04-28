## 정수를 담은 이차원 리스트, mylist 가 solution 함수의 파라미터로 주어집니다.
## solution 함수가 mylist 각 원소의 길이를 담은 리스트를 리턴하도록 빈칸을 완성해보세요.

def solution(mylist):
    answer = list(map(len, mylist))
    return answer

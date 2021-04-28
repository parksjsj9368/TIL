## 정수를 담은 이차원 리스트, mylist 가 solution 함수의 파라미터로 주어집니다.
## mylist에 들은 각 원소의 길이를 담은 리스트를 리턴하도록 solution 함수를 작성해주세요.

def solution(mylist):
    answer = []
    for i in mylist:
        answer.append(len(i))
    return answer


def solution(mylist):
    return list(map(len, mylist))

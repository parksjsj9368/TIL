# CH6. 알고리즘 (2)

<br>

<br>

## 6.1 삽입 정렬의 시간 복잡도

<br>

- 삽입 정렬 : 반드시 오름차순이 되도록 카드를 한 장씩 추가하며 배치하는 방법

<br>

``` PYTHON
# 삽입 정렬 코드
# 시간 복잡도 : for문,while문 루프가 총 2번 돌아서 O(n^2)
S = {1,4,6,3,2}

def insertionsort(S):
    for i in range(1, len(S)):
        card = S[i]
        j = i-1
        while(j-1 and S[j]>card):
            S[j+1] = S[j]
            j -= 1
        S[j+1] = card
    return S
print(interionsort(S))
```

<br>

<br>

## 6.2 병합 정렬의 시간 복잡도

<br>

- 병합 정렬 : 카드를 2장씩 묶어, 각각의 그룹을 오름차순으로 나열하고, 이번에는 두 그룹씩 선택해서 4장의 카드가 오름차순이 되도록 결합하는 동작을 반복하는 방법

<br>

``` python
# 병렬 정렬 코드
# 시간 복잡도 : 2분할과 루프의 곱 O(nlogn)
def mergesort(S):
    result = []
    if len(S) < 2:
        return S
    mid = int(len(S)/2)
    
    x = mergesort(S[:mid])
    y = mergesort(S[mid:])
    
    i, j = 0, 0
    while i<len(x) and j<len(y):
        if x[i]>y[i]:
            result.append(y[i])
            j += 1
        else:
            result.append(x[i])
            i += 1
    result += x[i:]
    result += y[j:]
    return result
```

<br>

<br>

## 6.3 퀵 정렬의 시간 복잡도

<br>

- 퀵 정렬 : 어떤 수를 기준으로 해서 그보다 큰값은 오른쪽에, 그 보다 작은 값이 왼쪽에 오도록 스왑하는 동작을 반복하는 방법

<br>

``` python
# 퀵 정렬 코드
# 시간 복잡도 : 2분할과 루프의 곱 O(nlogn) 
def quicksort(S):
    if len(S) == 1 or len(S) == 0:
        return S
    else:
        pivot = S[0]
        place = 0
        for j in range(len(S)-1):
            if S[j+1] < pivot:
                S[j+1], S[place+1] = S[place+1], S[j+1]
                place += 1
                
        S[0], S[place] = S[place], S[0]
        
        first = quicksort(S[:place])
        second = quicksort(S[place+1:])
        
        first.append(S[place])
        return first + second
```

<br>

<br>

## 6.4 공간 복잡도

<br>

- 공간 복잡도 : 알고리즘이 얼마만큼 컴퓨터 메모리를 차지하는지 나타내는 양

<br>

| 알고리즘                        | 알고리즘 특징                                                | 최선, 평균, 최악 <br />공간 복잡도 |
| ------------------------------- | ------------------------------------------------------------ | ---------------------------------- |
| 보고 정렬, 버블 정렬, 삽입 정렬 | 추가로 필요한 기억 영역이 없다                               | O(1)                               |
| 병합 정렬, 퀵 정렬              | 리스트를 분할해 갈때 원래 리스트와 같은 길이의 기억 영역이 추가로 필요하다 | O(n)                               |

<br>

<br>

## 6.5 정렬 알고리즘 정리

<br>

|           | 최선 시간 복잡도 | 평균 시간 복잡도 | 최악 시간 복잡도 | 공간 복잡도 |
| --------- | ---------------- | ---------------- | ---------------- | ----------- |
| 보고 정렬 | O(n)             | O((n+1)!)        | O((n+1)!)        | O(1)        |
| 버블 정렬 | O(n)             | O(n^2)           | O(n^2)           | O(1)        |
| 삽입 정렬 | O(n)             | O(n^2)           | O(n^2)           | O(1)        |
| 병합 정렬 | O(nlogn)         | O(nlogn)         | O(nlogn)         | O(n)        |
| 퀵 정렬   | O(nlogn)         | O(nlogn)         | O(n^2)           | O(n)        |

<br>
# 18강. DFS 알고리즘

<br>

<br>

## DFS(Depth-First Search)

<br>

<br>

### DFS

<br>

- **깊이 우선 탐색 = 깊은 부분을 우선적으로 탐색하는 알고리즘**

- **스택 자료구조(혹은 재귀함수)를 이용**

<br>

- 구체적인 동작 과정
  1. 탐색 시작 노드를 스택에 삽입하고 방문 처리
  2. 스택의 최상단 노드에 방문하지 않은 노드가 하나라도 있다면 그 노드를 스택에 넣고 방문 처리. 방문하지 않은 노드가 없으면 스택에서 최상단 노드를 꺼낸다
  3. 더 이상 2번의 과정을 수행 할 수 없을 때까지 반복

<br>

<br>

### DFS 동작 예시

<br>

<br>

- 방문 기준 : 번호가 낮은 인접 노드부터

<br>

![](C:\Users\user\Desktop\TIL\ALGORITHM\LECTURE\L18_DFS 알고리즘.assets\L18_1.PNG)

<br>

- 탐색 순서 : 1 -> 2 -> 7 -> 6 -> 8 -> 3 -> 4 -> 5

<br>

<br>

```python
# DFS 메서드 정의
def dfs(graph, v, visited) :
	
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end="")
    
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v] :
        if not visited[i] :
            dfs(graph, i, visited)
      
    
# 각 노드가 연결되 정보를 표현 (2차원 리스트)
graph = [
    [],
    # 1번 노드와 연결된 리스트
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

# 각 노드가 방문된 정보를 표현 (1차원 리스트)
visited = [False]*9

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)
```

<br>
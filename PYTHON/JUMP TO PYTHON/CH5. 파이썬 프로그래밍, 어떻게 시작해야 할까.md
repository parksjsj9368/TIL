# CH5. 파이썬 프로그래밍, 어떻게 시작해야 할까?

<br>

<br>

## 5.1 3과 5의 배수 합하기

<br>

- **문제 : 1000 미만의 자연수에서 3의 배수와 5의 배수의 총합을 구하라**

<br>

``` python
i = 0
data = []

while i < 1000
	i += 1
    if (i % 3 == 0) | (i % 5 == 0):
        data.append(i)

result = sum(data)
```

<br>

<br>

## 5.2 게시판 페이징하기

<br>

- **문제 : A 씨는 게시판 프로그램을 작성하고 있다. 그런데 게시물의 총 건수와 한 페이지에 보여줄 게시물 수를 입력으로 주었을 때 총 페이지수를 출력하라**

<br>

``` PYTHON
def getTotalPage(m, n):
   	if m // n == 0:
        return m // n
    else:
	    return m // n + 1
```

<br>

<br>

## 5.3 간단한 메모장 만들기

<br>

- **문제 : 원하는 메모를 파일에 저장하고 추가 및 조회가 가능한 간단한 메모장을 만들어 보자**

<br>

``` python
import sys
option = sys.argv[1]

if option == 'a':
    memo = sys.argv[2]
    f = open('memo.txt', 'a')
    f.write(memo)
    f.write('\n')
    f.close()
elif option == 'v':
    f = open('memo.txt')
    memo = f.read()
    f.close()
    print(memo)
```

<br>

<br>

## 5.4 탭을 4개의 공백으로 바꾸기

<br>

- **문제 : 문서 파일을 읽어서 그 문서 파일 내에 있는 탭을 공백 4개로 바꾸어주자**

<br>

``` python
import sys
src = sys.argv[1]
dst = sys.argv[2]

f = open(src)
tab_content = f.read()
f.close()
space_content = tab_content.replace('\t',' '*4)

f = open(dst, 'w')
f.write(space_content)
f.close()
```

<br>

<br>

## 5.5 하위 디렉터리 검색하기

<br>

- **특정 디렉터리부터 시작해서 그 하위의 모든 파일 중 파이썬 파일만 출력해보자**

<br>

``` python
import os

def search(dirname):
    try:
        filenames = os.listdir(dirname)
        
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)
            
            if os.path.isdir(full_filename):
                search(full_filename)
            else:
                ext = os.path.splitext(full_filename)[-1]
                if ext == '.py':
                    print(full_filename)
                    
    except PermissionError:
        pass
```

<br>
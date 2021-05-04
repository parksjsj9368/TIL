# CH3. 프로그래밍의 입력과 출력은 어떻게 해야 할까?

<br>

<br>

## 3.1 함수

<br>

- 파이썬 함수의 구조

def 함수명(입력 인수):

​	수행할 문장

​	return 결과값

<br>

- 입력값이 몇 개가 될지 모를때

def 함수명(*입력변수):

​	수행할 문장

<br>

<br>

- 함수 안에서 함수 밖의 변수를 변경하는 방법

<br>

``` python
a = 1
def vartest(a):
    a = a+1
    return a
a = vertest(a) # vartest(a)의 결과값을 함수 밖의 변수 a에 대입
a # 2

a = 1
def vartest():
    global a
    a = a+1
vartest()
a # 2
```

<br>

<br>

## 3.2 사용자 입력과 출려

<br>

``` python
a = input() # 입력
print(a) # 출력
```

<br>

<br>

## 3.3 파일 읽고 쓰기

<br>

| 파일 열기 모드 | 설명      |
| -------------- | --------- |
| r              | 읽기 모드 |
| w              | 쓰기 모드 |
| a              | 추가 모드 |

<br>

<br>

## 파일 읽기

<br>

``` python
f = open('새파일.txt', 'r')
f.close()
```

<br>

<br>

### 프로그램의 외부에 저장된 파일을 읽는 여러가지 방법

<br>

- readline() 함수 이용하기

``` python
f = open('새파일.txt', 'w')
line = f.readline()
print(line) # 1번째 줄입니다
f.close()
```

<br>

- readlines() 함수 이용하기

``` python
f = open('새파일.txt', 'w')
lines = f.readlines()
print(lines) # ['1번째 줄입니다','2번째 줄입니다',,,,]
f.close()
```

<br>

- read() 함수 이용하기

``` python
f = open('새파일.txt', 'w')
data = f.read()
print(data)
f.close()
```

<br>

<br>

## 파일 쓰기

<br>

### 파일 생성하기

<br>

``` python
f = open('새파일.txt', 'w')
f.close()
```

<br>

<br>

### 파일을 쓰기 모드로 열어 출력값 적기

<br>

``` python
f = open('새파일.txt', 'w')
for i in range(1,11):
    data = "%d번째 줄입니다.\n" %i
    f.write(data)
f.close()
```

<br>

<br>

### with 문과 함께 사용하기

<br>

``` python
with open('새파일.txt', 'w') as f:
    f.write('Life is too short, you need python')
```

<br>

<br>

## 파일 내용 추가하기

<br>

### 파일에 새로운 내용 추가하기

<br>

``` python
f = open('새파일.txt', 'a')
for i in range(1,11):
    data = "%d번째 줄입니다.\n" %i
    f.write(data)
f.close()
```

<br>
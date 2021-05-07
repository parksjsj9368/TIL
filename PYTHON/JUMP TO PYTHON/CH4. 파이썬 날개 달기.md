# CH4. 파이썬 날개 달기

<br>

<br>

## 4.1 파이썬 프로그래밍의 핵심, 클래스

<br>

<br>

## 4.2 모듈

<br>

<br>

## 4.3 패키지

<br>

<br>

## 4.4 예외 처리

<br>

### 오류 예외 처리 기법

<br>

- try, except 문

``` python
try:
    ...
except [발생오류 [as 오류 메시지 변수]]:
    ...

try:
    4/0
except ZeroDivisionError as e:
    print(e)
```

<br>

- try, else 문

: try문은 else절을 지원한다. else절은 예외가 발생하지 않은 경우에 실행되며 반드시 except 절 바로 다음에 위치한다

``` python
try:
    f = open('foo.txt', 'r')
except FileNotFoundError as e:
    print(str(e))
else:
    data = f.read()
    f.close()
```

<br>

- try, except 문

: try문에는 finally절을 사용할 수 있다. finally절은 try문 수행 도중 예외 발생 여부에 상관없이 항상 수행된다

``` python
f = open('foo.txt','w')
try:
    # 무언가를 수행한다
finally:
    f.close()
```

<br>

<br>

### 오류 회피하기

<br>

- pass 활용

``` python
try:
    f = open('나없는파일','r')
except FileNotFoundError:
    pass
```

<br>

<br>

### 오류 일부러 발생시키기

<br>

- raise 명령어 : 오류를 강제로 발생

``` python
class Bird:
    def fly(self):
        raise NotImplementedError
```



<br>

<br>

## 4.5 내장 함수

<br>

| 함수       | 특징                                                         | 파이썬 사용 예                                               |
| ---------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| abs        | 숫자의 절대값을 돌려주는 함수                                |                                                              |
| all        | x가 모두 참이면 True, 거짓이 하나라도 있으면 False를 리턴    | allI([1,2,3,0]) # False                                      |
| any        | x 중 하나라도 참이 있을 경우 True, 모두 거짓일 경우에만 False 리턴 | any([1,2,3,0]) # True                                        |
| chr        | 아스키 코드값을 입력으로 받아 그 코드에 해당하는 문자를 출력하는 함수 | chr(97) # 'a'                                                |
| dir        | 객체가 자체적으로 가지고 있는 변수나 함수를 보여준다         |                                                              |
| divmod     | 2개의 숫자를 입력으로 받아, a를 b로 나눈 몫과 나머지를 튜플 형태로 리턴 | divmod(7,3) # (2,1)                                          |
| enumerate  | for문과 함께 자료형의 현재 인덱스값과 함께 리턴              | for i , name in enumerate(['body','foo']): print(i, name)    |
| eval       | 실행 가능한 문자열을 입력으로 받아 문자열을 실행             | eval('1+2') # 3                                              |
| filter     | 첫 번째 인수로 함수 이름을, 두 번째 인수로 그 함수에 차례로 들어갈 반복 가능한 자료형을 받아 걸러내는 함수 | def positive(x) : return x>0<br />print(list(filter(positive,[1,-3,2,0,-5,6])))<br /><br />print(list(filter(lambda x:x>0, [1,-3,2,0,-5,6]))) |
| hex        | 정수값을 입력 받아 16진수로 변환하여 리턴하는 함수           | hex(234) # '0xea'                                            |
| input      | 사용자 입력을 받는 함수                                      |                                                              |
| int        | 문자열 형태의 숫자나 소수점이 있는 숫자 등을 정수 형태로 리턴하는 함수, int(x,radix)는 radix진수로 표현된 문자열 x를 10진수로 변환하여 리턴 | int('3') # 3<br />int('11', 2) # 3                           |
| isinstance | 첫 번째 인수로는 인스턴스, 두 번째 인수로 클래스 이름을 받는다. 입력 받은 인스턴스가 그 클래스의 인스턴스인지 판단하는 함수 | class Person: pass<br />a = Person()<br />isinstance(a, Person) # True |
| lambda     | 함수를 생성할 때 사용하는 예약어로, def와 동일한 역할        | sum = lambda a, b : a+b<br />sum(3,4) # 7                    |
| len        | 입력값 s의 길이를 리턴                                       |                                                              |
| list       | 반복 가능한 자료형 s를 입력 받아 리스트로 만들어 리턴        |                                                              |
| map        | 함수와 반복 가능한 자료형을 입력으로 받는다                  | list(map(lambda a:a*2, [1,2,3,4]))<br />[2,4,6,8]            |
| max        | 최대값을 리턴하는 함수                                       |                                                              |
| min        | 최소값을 리턴하는 함수                                       |                                                              |
| oct        | 정수 형태의 숫자를 8진수 문자열로 바꾸어 리턴                | oct(34) # '0o42'                                             |
| open       | open(file, [mode])로 파일객체를 리턴하는 함수                |                                                              |
| ord        | 문자의 아스키 코드값을 리턴하는 함수                         | ord('a') # 97                                                |
| pow        | x의 y제곱한 결과값을 리턴하는 함수                           | pow(2,4) # 16                                                |
| range      | range([start], stop, [,step])                                | list(range(1,10,2))<br />[1,3,5,7,9]                         |
| sorted     | 입력값을 정렬한 후 그 결과를 리스트로 리턴                   |                                                              |
| str        | 문자열 형태로 객체를 변환하여 리터                           |                                                              |
| tuple      | 튜플 형태로 바꾸어 리턴하는 함수                             |                                                              |
| type       | 입력값의 자료형이 무엇인지 알려주는 함수                     |                                                              |
| zip        | 동일한 개수로 이루어진 자료형을 묶어 주는 역할 하는 함수     | list(zip([1,2,3],[4,5,6])) #[(1,4),(2,5),(3,6)]              |

<br>

<br>

## 4.6 외장 함수

<br>

### sys

<br>

- sys 모듈은 파이썬 인터프리터가 제공하는 변수들과 함수들을 직접 제어할 수 있게 해주는 모듈

<br>

- 명령 행에서 인수 전달하기 : sys.argv
- 강제로 스크립트 종료하기 : sys.exit
- 자신이 만든 모듈 불러와 사용하기 : sys.path

<br>

<br>

### pickle

<br>

- pickle은 객체의 형태를 그대로 유지하면서 파일에 저장하고 불러올 수 있게 하는 모듈

<br>

``` python
import pickle
f = open('text.txt', 'wb')
data = {1:'python', 2:'you need'}
pickle.dump(data, f)
f.close()

import pickle
f = open('text.txt', 'rb')
data = pickle.load(f)
print(data) # {2:'you need', 1:'python'}
```

<br>

<br>

### OS 모듈

<br>

- OS 모듈은 환경 변수나 디렉터리, 파일 등의 OS 자원을 제어할 수 있게 해주는 모듈

<br>

- 내 시스템의 환경 변수값을 알고 싶을 때 : os.environ
- 디렉터리 위치 변경하기 : os.chdir
- 디렉터리 위치 리턴받기 : os.getcwd
- 시스템 명령어 호출하기 : os.system
- 실행한 시스템 명령어의 결과값 리턴받기 : os.popen
- 디렉터리 생성 : os.mkdir
- 디렉터리 삭제(단 디렉터리가 비어있다면) : os.rmdir
- 파일 삭제 : os.unlink
- src라는 이름의 파일을 dst라는 이름으로 변경 : os.rename(src, dst)

<br>

<br>

### shutil

<br>

- shutil은 파일을 복사해 주는 파이썬 모듈

<br>

- 파일 복사 : shutil.copy(src, dst)

<br>

<br>

### glob

<br>

- 가끔 파일을 읽고 쓰는 기능이 있는 프로그램을 만들다 보면 특정 디렉터리에 있는 파일 이름 모두를 알아야 할 때가 있다. 이럴 떄 사용하는 모듈

<br>

- 디렉터리에 이쓴 ㄴ파일들을 리스트로 만들기 : glob(pathname)

<br>

<br>

### tempfile

<br>

- 파일을 임시로 만들어서 사용할 때 유용한 모듈

<br>

- 중복되지 않는 임시 파일의 이름을 무작위로 리턴 : tempfile.mktemp()
- 임시 저장 공간으로 사용될 파일 객체를 리턴 : tempfile.TemporaryFile()

<br>

<br>

### time

<br>

- 시간과 관련된 time 모듈

<br>

- UTC 이용하여 현재 시간을 실수 형태로 리턴 : time.time
- time.time()에 의해서 반환된 실수값을 년월일 형태로 리턴 : time.localtime
- time.localtime에 의해서 반환된 튜플 형태의 값을 인수로 받아서 알아보기 쉽게 리턴 : time.asctime
- time.asctime(time.localtime(time.time())) = time.ctime()
- 여러 가지 포맷 코드를 통해 표현 : time.strftime
- 일정한 시간 간격을 두고 루프를 실행 : time.sleep

<br>

<br>

### calendar

<br>

- calendar는 파이썬에서 달력을 볼 수 있게 해주는 모듈

<br>

- 그 해의 전체 달력 : calendar.calendar(연도)
- 그 해의 전체 달력 : calendar.prcal(연도)
- 해당 년, 월의 달력 : calendar.prmonth(년, 월)
- 해당 하는 요일 정보를 리턴 (월 0 ~ 일 6) : calendar.weekday(년, 월, 일)
- 해당 년, 월의 1일이 무슨 요일인지, 몇일 까지 있는지 튜플로 리턴 : calendar.monthrange(년, 월)

<br>

<br>

### random

<br>

- random은 난수를 발생시키는 모듈

<br>

- 실수 중에서 난수값 리턴 : random.random()
- 정수 중에서 난수 값 리턴 : random.randomint()
- 리스트 항목을 무작위로 섞고 싶을 때 : random.shuffle()

<br>

<br>

### webbrowser

<br>

- webbrowser는 자신의 시스템에서 사용하는 기본 웹 브라우저가 자동으로 실행되게 하는 모듈

<br>


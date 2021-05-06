# CH4. 파이썬 날개 달기

<br>

<br>

## 4.1 파이썬 프로그래밍의 핵심, 클래스

<br>

- 클래스 : 똑같은 무엇인가를 계속해서 만들어낼 수 있는 설계 도면 같은 것

- 객체(=인스턴스) : 클래스에 의해서 만들어진 피조물



<br>

<br>

## 4.2 모듈

<br>



<br>

<br>

## 4.3 패키지

<br>



<br>

<br>

## 4.4 예외 처리

<br>



<br>

<br>

## 4.5 내장 함수

<br>



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


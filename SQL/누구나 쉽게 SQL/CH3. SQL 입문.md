# CH3. SQL 입문

<br>

<br>

## 3.1 SQL(=Structed Query Language) 이란?

<br>

- SQL : 구조적인 질의 언어, RDBMS와 소통하는 프로그래밍 언어

1. 질의 언어 : SQL은 데이터베이스를 상대로 데이터를 조회, 입력, 수정, 삭제하기 위해 사용

2. 집합적 언어: 데이터를 한 건씩 처리하는게 아니라 조건에 맞는 데이터 전체를 한 번에 처리

<br>

<br>

## 3.2 SQL 표준

<br>

- SQL 표준 : ANSI와 ISO

<br>

RDBMS 제조사에 상관없이 SQL을 동일한 형태로 사용할 수 있는 ANSI를 만들었으나, 그전에 제품을 출시하여서 ANSI와 충돌이 불가피해졌다 그래서 RDBMS 제품별로 SQL 사용법에는 차이가 있다

<br>

<br>

## 3.3 SQL의 종류

<br>

SQL이 처리하는 문장의 성격에 따라 분류한 것

<br>

<br>

### 1. DDL (=Data Definition Language, 데이터 정의어)

RDBMS에는 테이블 외에도 뷰, 인덱스, 시퀀스 등 여러 객체가 있는데, 이를 **생성하고 삭제하고 수정하는 sql**

<br>

- CREATE : 객체 생성

- DROP : 객체 삭제
- ALTER : 객체 변경
- TRUNCATE TABLE : 테이블에 있는 모든 데이터 삭제
- RENAME : 객체 이름 변경

<br>

<br>

### 2. DML (=Data Manipulation Language, 데이터 조작어)

데이터를 직접 조작하는 sql

<br>

- SELECT : 테이블이나 뷰에서 데이터 조회
- INSER : 데이터 입력
- UPDATE : 기존 데이터 수정
- DELETE : 테이블에 있는 데이터 삭제
- MERGE : 조건에 따라 INSERT와 UPDATE 수행

<br>

** **TRUNCATE와 DELETE의 차이** **

TRUNCATE는 실행하면 모든 데이터가 사라져 돌이킬 수 없고, DELETE는 선별 삭제되며 삭제 이전으로 복원 가능

<br>

<br>

### 3. TCL (=Transaction Control Language, 트랜잭션 제어어)

트랜잭션을 처리하는 sql

DML(데이터 변경하는 문장)의 실수를 방지하기 위해 한 번 더 체크하는 기능

<br>

- COMMIT : DML로 변경된 데이터를 COMMIT 해야 최종적으로 DB에 적용
- ROLLBACK : DML로 변경된 데이터를 변경 이전 상태로 되돌린다

<br>

<br>

### 4. DCL (=Data Control Language, 데이터 제어어)

객체에 대한 권한을 할당하거나 회수하는 sql

<br>

- GRANT : 객체에 대한 권한 할당

- REVOKE : 객체에 할당된 권한을 회수

<br>

<br>

## 3.4 테이블 생성

<br>

- DML의 CREATE 테이블 생성 구문

<br>

``` mysql
CREATE TABLE table_name(
	column_name1 datatype [NOT] NULL,
    column_name2 datatype [NOT] NULL,
    ...
    PRIMARY KEY ( column_list )
);
```

<br>

<br>

- 테이블 이름과 컬럼 이름

1. 30 byte (영어 기준) 넘지 않는다

2. 언너스코어(_), 문자, 숫자를 사용할 수 있지만 이름의 첫 문자는 반드시 문자

<br>

- 컬럼의 데이터형

1. 문자형 

   1. CHAR(n) : 고정 길이 문자(무조건 설정한 크기로 고정), 최대 2000 byte
   2. VARCHAR2(n) : 가변 길이 문자, 최대 4000 byte

2. 숫자형

   NUMBER[ (p, [s]) ]

3. 날짜형

   DATE

<br>

- NULL

NULL은 데이터가 없음을 의미

NOT NULL로 명시한 컬럼에 값을 넣지 않으면 입력 시 오류가 발생해 입력 작업이 취소

<br>

- 기본 키

테이블 당 1개(컬럼 1개 또는 여러 컬럼 결합) 만들 수 있다

기본 키 컬럼에는 반드시 NOT NULL 명시

<br>

<br>

``` mysql
# emp03 테이블 생성
CREATE TABLE emp03 (
	emp_id		NUMBER			NOTNULL,
    emp_name	VARCHAR2(100)	NOTNULL,
    gender		VARCHAR2(10)	NULL,
    age			NUMBER			NULL,
    hire_date	DATE			NULL,
    etc			VARCHAR2(300)	NULL,
    PRIMARY KEY (emp_id)
);


# emp03 테이블 조회
SELECT *
	FROM emp03;
```

<br>
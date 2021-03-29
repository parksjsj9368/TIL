# CH4. 데이터 입력과 삭제

<br>

<br>

## 4.1 데이터 입력, INSERT 문

<br>

- DML의 INSERT 데이터 입력 구문

<br>

``` MYSQL
# INSERT 구문 1
# 특정 컬럼만 선택해 데이터를 넣는다
INSERT INTO 테이블명 ( column1, column2, column4 ... )
VALUES ( 값1, 값2, 값4 ... );


# INSERT 구문 2
# 모든 컬럼에 데이터를 넣는다, 컬럼 순서는 데이블 생성할 때 순서와 같게
INSERT INTO 테이블명
VALUES ( 값1, 값2, 값3 ...);


# INSERT 구문 3
# 한 문장당 한개의 로우가 아닌 여러 개의 로우 입력
INSERT INTO 테이블명 ( column1, column2, ... )
SELECT 문장;


# 데이터 입력이 완료되고 확인이 끝나면 반드시 COMMIT 문
COMMIT;
```

<br>

<br>

## 4.2 데이터 삭제, DELETE 문

<br>

``` MYSQL
# DELETE 구문
# WHERE 절을 생략하면 테이블에 있는 모든 데이터를 삭제
DELETE [FROM] 테이블명
WHERE 조건;


# 데이터를 잘못 삭제 했다면 이전 상태로 되돌리는 ROLLBACK 문
ROLLBACK;
```

<br>

<br>

## 4.3 테이블 생성과 데이터 입력 실습

<br>

``` MYSQL
# subway_statistics 테이블 생성
CREATE TABLE subway_statistics (
	seq_id				NUMBER			NOT NULL	PRIMARY KEY,
    station_name		VARCHAR2(100)	NULL,
    boarding_date		DATE			NULL,
    gubun				VARCHAR2(10)	NULL,
    boarding_time		NUMBER			NULL,
    passenger_number	NUMBER			NULL
);


# subway_statistics 테이블 데이터 입력
INSERT INTO subway_statistics VALUES (1, '서울역(150)', '2017-04-01', '승차', 7, 654);
INSERT INTO subway_statistics VALUES (2, '서울역(150)', '2017-04-01', '하차', 7, 1923);
INSERT INTO subway_statistics VALUES (3, '서울역(150)', '2017-04-02', '승차', 7, 413);
```

<br>


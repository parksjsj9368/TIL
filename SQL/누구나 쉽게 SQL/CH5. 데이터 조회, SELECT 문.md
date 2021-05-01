# CH5. 데이터 조회, SELECT 문

<br>

<br>

## 5.1 SELECT 문의 기본 구문

<br>

- DML의 SELECT 테이블에 있는 데이터를 조회하는 구문

<br>

``` MYSQL
# SELECT 구문
SELECT column1, column2, ...
FROM 테이블명
WHERE 조건
ORDER BY 정렬 순서;
```

<br>

<br>

### 1. SELECT 절

<br>

- 테이블에서 선택한 컬럼이나 표현식을 명시

1. 선택한 컬럼
   1. 컬럼명 선택 : 명시한 컬럼 순서대로 데이터 가져온다
   2. 전체 컬럼 선택 : \*
2. 표현식 명시

하나 이상의 값, 연산자, sql 함수가 결합된 식

<br>

<br>

### 2. FROM 절

<br>

- 조회 하고자 하는 테이블명

- 여러 개의 테이블을 가져올 때는 FROM 절에 콤마로 구분

<br>

<br>

### 3. WHERE 절

<br>

- 테이블의 데이터 중 특정 조건에 맞는 데이터를 가져오고자 할 때 조건을 기술
- WHERE 절은 생략 가능한데 생략하면 모든 데이터를 가져온다

<br>

<br>

### 4. ORDER 절

<br>

- 조회한 데이터를 정렬해서 보여주는 역할
- 기본적으로 오름차순으로 정렬

<br>

<br>

## 5.2 조건에 맞는 데이터 조회하기

<br>

### 1. 조건 연산자

<br>

| 조건 연산자 | 기능                                      |
| ----------- | ----------------------------------------- |
| =           | 두 값이 같을 때 참                        |
| !=, <>      | 두 값이 다를 때 참                        |
| >           | 왼쪽 값이 오른쪽 값보다 클 때 참          |
| <           | 왼쪽 값이 오른쪽 값보다 작을 때 참        |
| >=          | 왼쪽 값이 오른쪽 값보다 크거나 같을 때 참 |
| <=          | 왼쪽 값이 오른쪽 값보다 작거나 같을 떄 참 |

<br>

- AND 연산자 : 2개 이상의 조건을 연결 할 때, 조건 모두 만족
- OR 연산자 : 조건 중 하나만 만족

<br>

``` MYSQL
# 잠실역에서 7시나 9시에 승하차한 건을 조회 하는 쿼리
SELECT *
	FROM subway_statistics
WHERE	station_name = '잠실(216)'
	AND	(	boarding_time = 7
        OR	boarding_time = 9);
```

<br>

<br>

### 2. LIKE 연산자

<br>

``` mysql
# 선릉역 조회
# %는 모든 것을 의미
WHERE station_name LIKE '선릉%'
```

<br>

<br>

### 3. IN 연산자

<br>

- OR과 같은 기능을 하는 IN 연산자

<br>

``` mysql
# 잠실역에서 7시나 9시에 승하차한 건을 조회 하는 쿼리
SELECT *
	FROM subway_statistics
WHERE	station_name = '잠실(216)'
	AND	boarding_time IN (7,9);
```

<br>

<br>

### 4. BETWEEN 연산자

<br>

``` mysql
SELECT *
	FROM subway_statistics
WHERE 	station_name LIKE '선릉%'
	AND	(passenger_number BETWEEN 500 AND 1000);
```

<br>

<br>

## 5.3 데이터 정렬하기

<br>

| ORDER BY  절 형태            | 정렬 방식                                                    |
| ---------------------------- | ------------------------------------------------------------ |
| ORDER BY col1, col2          | col1 오름차순 후, col2 오름차순 정렬                         |
| ORDER BY col1 DESC, col2     | col1 내림차순 후, col2 오름차순 정렬                         |
| ORDER BY col2 ASC, col1 DESC | col2 오름차순 후, col1 내림차순 정렬                         |
| ORDER BY 1, 2                | SELECT 절에 명시한 첫 번째와 두 번째 컬럼을 순서대로 오름차순 정렬 |

<br>
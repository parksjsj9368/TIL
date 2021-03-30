# CH8. 집합 쿼리

<br>

<br>

## 8.1 UNION ALL

<br>

- UNION ALL : 두 집합의 모든 원소를 가져오는 합집합 역할

<br>

``` mysql
# UNION ALL 구문
SELECT col1, col2
	FROM ...
WHERE ...
UNION ALL
SELECT col1, col2
	FROM ...
WHERE ...
```

<br>

- 컬럼 수가 다르거나, 컬럼 데이터형이 다른 경우에는 오류가 발생한다
- SELECT 절에 명시하는 컬럼의 이름은 달라도 상관 없다, 최종 결과엔 첫번째 SELECT문의 컬럼 명을 따른다
- 반환 컬럼 값 모두를 체크해 중복이여도 여러번 조회 허용
- 집합 연산자를 사용하고 쿼리에서 데이터 정렬이 가능하다

<br>

<br>

## 8.2 UNION

<br>

- UNION : UNION ALL과 다르게 반환 컬럼 값 모두가 중복이라면 1건만 조회한다

<br>

``` mysql
# UNION 구문
SELECT col1, col2
	FROM ...
WHERE ...
UNION
SELECT col1, col2
	FROM ...
WHERE ...
```

<br>

<br>

## 8.3 INTERSECT

<br>

- INTERSECT : 두 집합의 공통 원소만 추출하는 교집합 역할

<br>

``` mysql
# INTERSECT 구문
SELECT col1, col2
	FROM ...
WHERE ...
INTERSECT
SELECT col1, col2
	FROM ...
WHERE ...
```

<br>

<br>

## 8.4 MINUS

<br>

- MINUS : 한 집합을 기준으로 다른 집합에 없는 요소만 추출하는 차집합 역할

<br>

``` mysql
# MINUS 구문
SELECT col1, col2
	FROM ...
WHERE ...
MINUS
SELECT col1, col2
	FROM ...
WHERE ...
```

<br>
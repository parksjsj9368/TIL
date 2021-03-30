# CH7. 데이터 집계

<br>

<br>

## 7.1 GROUP BY 절과 집계 함수

<br>

<br>

### 1. GROUP BY 절

<br>

``` mysql
# GROUP BY 절 구문
SELECT expr1, expr2, ...
	FROM ...
WHERE ...
	AND ...
GROUP BY expr1, expr2, ...
ORDER BY ...
```

<br>

``` mysql
# subway_statistics 테이블에서 구분이 '승차'인 데이터만 station_name으로 그룹지어 이름 순으로 정렬해라
SELECT	station_name
	FROM	subway_statistics
WHERE	gubun = '승차'
GROUP BY station_name
ORDER BY station_name;
```

<br>

- SELECT 절에 'DISTINCT 컬럼 명' 형태로 사용하면 해당 컬럼에 들어 있는 값에서 중복 값을 제외한 유일한 값들만 조회되어 GROUP BY 절을 사용한 효과가 난다

<br>

<br>

### 2. 집계 함수

<br>

| 함수 명          | 기능                                                         |
| ---------------- | ------------------------------------------------------------ |
| COUNT( expr )    | expr의 전체 개수를 구해 반환,<br />expr을 \* 로 사용하면 조회된 전체 데이터 건수를 반환 |
| MAX( expr )      | expr의 최댓값을 반환                                         |
| MIN( expr )      | expr의 최솟값을 반환                                         |
| SUM( expr )      | expr의 합계를 반환                                           |
| AVG( expr )      | expr의 평균값을 반환                                         |
| VARIANCE( expr ) | expr의 분산을 반환                                           |
| STDEV( expr )    | expr의 표준편차를 반환                                       |

<br>

<br>

## 7.2 HAVING 절

<br>

- HAVING 절은 GROUP BY 절과 함께 사용되며 집계 함수 결과 값으로 조건을 걸 때 사용된다

<br>

<br>

<br>

## 세진 정리

<br>

1. **FROM** : SQL은 구문이 들어오면 **테이블을 가장 먼저 확인**합니다.

2. **WHERE** : 테이블명을 확인했으니, **테이블에서 주어진 조건에 맞는 데이터들을 추출**해줍니다.

3. **GROUP BY** : 조건에 맞는 데이터가 추출되었으니, **공통적인 데이터들끼리 묶어 그룹**을 만들어줍니다.

4.  **HAVING** : 공통적인 데이터들이 묶여진 그룹 중, **주어진 주건에 맞는 그룹들을 추출**해줍니다.

5. **SELECT** : 최종적으로 **추출된 데이터들을 조회**합니다.

6. **ORDER BY** : 추출된 데이터들을 **정렬**해줍니다.

<br>
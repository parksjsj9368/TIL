# CH6. SQL 연산자와 함수

<br>

<br>

## 6.1 SQL 연산자

<br>

- 기본 연산자

<br>

| 연산자 | 설명                       |
| ------ | -------------------------- |
| +      | 두 수나 두 날짜를 더함     |
| -      | 두 수나 두 날짜를 뺌       |
| *      | 두 수를 곱함               |
| /      | 왼쪽 수를 오른쪽 수로 나눔 |
| \|\|   | 두 문자를 결합함           |

<br>

<br>

## 6.2 주요 SQL 함수

<br>

<br>

### 1. 숫자형 함수

<br>

| 함수 명         | 기능                                                         | 사용 예                                               |
| --------------- | ------------------------------------------------------------ | ----------------------------------------------------- |
| ABS( n )        | n의 절댓값을 반환                                            | SELECT ABS(-1)<br />FROM DAUL;<br />=> 1              |
| CEIL( n )       | n과 같거나 큰 최소 정수 반환, 올림                           | SELECT CEIL(10.6)<br />FROM DAUL;<br />=> 11          |
| EXP( n )        | e(e=2.71828183...)의 n승을 반환                              | SELECT EXP(10)<br />FROM DAUL;<br />=> 22026.4657     |
| FLOOR( n )      | n과 같거나 작은 최대 정수 반환, 내림                         | SELECT FLOOR(10.6)<br />FROM DAUL;<br />=> 10         |
| LN( n )         | n의 자연고르 값 반환                                         | SELECT LN(10)<br />FROM DAUL;<br />=> 2.302585        |
| LOG( n2, n1 )   | n2는 밑, n1은 진수                                           | SELECT LOG(10, 100)<br />FROM DAUL;<br />=> 2         |
| MOD( n2, n1 )   | n2를 n1으로 나눈 나머지 반환                                 | SELECT MOD(11, 4)<br />FROM DAUL;<br />=> 3           |
| POWER( n2, n1 ) | n2의 n1승을 반환                                             | SELECT POWER(3, 2)<br />FROM DAUL;<br />=> 9          |
| ROUND( n, i )   | n의 소수점 기준 i+1번째에서 반올림                           | SELECT ROUND(10.545, 2)<br />FROM DAUL;<br />=> 10.55 |
| SIGN( n )       | n의 부호 반환,<br />n이 양수면 1 음수면 -1 0이면 0 반환      | SELECT SIGN(-110)<br />FROM DAUL;<br />=> -1          |
| SQRT( n )       | n의 제곱근 값 반환                                           | SELECT SQRT(2)<br />FROM DAUL;<br />=> 1.414213       |
| TRUNC( n1, n2 ) | n1의 소수점 기준 n2 자리에서 절삭,<br />n2 생략시 0으로 인지 | SELECT TRUNC(10.545, 2)<br />FROM DAUL;<br />=> 10.54 |

<br>

<br>

### 2. 문자형 함수

<br>

| 함수명                  | 기능                                                         | 사용 예                                                      |
| ----------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| CHR ( n )               | n은 숫자로 n 값에 해당되는 문자를 반환                       | SELECT CHR(65) \|\| CHR(66) \|\| CHR(67)<br />FROM DAUL;<br />=> ABC |
| CONCAT( char1, char2 )  | char1과 char2 문자를 결합한 결과를 반환,<br />\|\|과 같은 기능 | SELECT CONCAT('A', 'B')<br />FROM DAUL;<br />=> AB           |
| INITCAP( char )         | char의 첫 번쨰 문자를 대문자로 변환                          | SELECT INITCAP('the')<br />FROM DAUL;<br />=> The            |
| LOWER( char )           | char을 소문자로 변환                                         | SELECT LOWER(THE)<br />FROM DAUL;<br />=> the                |
| UPPER( char )           | char을 대문자로 변환                                         | SELECT UPPER(the)<br />FROM DAUL;<br />=> THE                |
| LPAD( expr1, n, expr2 ) | expr1을 반환하는데 expr2를 (n-expr1 길이)만큼 왼쪽으로 채워서 반환 | SELECT LPAD('THE', 5, '*')<br />FROM DAUL;<br />=> **THE     |
| RPAD( expr1, n, expr2)  | expr1을 반환하는데 expr2를 (n-expr1 길이)만큼 오른쪽으로 채워서 반환 | SELECT RPAD('THE', 5, '*')<br />FROM DAUL;<br />=> THE**     |
| LTRIM( expr1, expr2 )   | expr1의 왼쪽에서 expr2를 제거한 결과를 반환                  | SELECT LTRIM('\*\*THE\*\*', '*')<br />FROM DAUL;<br />=> THE** |
| RTRIM( expr1, expr2 )   | expr1의 오른쪽에서 expr2를 제거한 결과를 반환                | SELECT RTRIM('\*\*THE\*\*', '*')<br />FROM DAUL;<br />=> **THE |
| SUBSTR( char, n1, n2 )  | char에서 n1 위치에서 시작해 n2 길이 만큼 잘라낸 결과 반환<br />n1을 0으로 명시하면 1이 적용<br />n1이 음수이면 char 오른쪽 끝에서부터 거꾸로 세어 가져옴<br />n2를 생략하면 n1부터 끝까지 반환<br />n2 값을 1미만으로 지정하면 NULL을 반환 | SELECT SUBSTR('ABCDEFG', 3, 2)<br />FROM DAUL;<br />=> CD<br /><br />SELECT SUBSTR('ABCDEFG',-3)<br />FROM DAUL;<br />=> EFG |
| TRIM( char )            | char의 양쪽 끝 공백을 제거한 결과를 반환                     | SELECT TRIM('     ABC D     ')<br />FROM DAUL;<br />=> ABC D |

<br>

| 함수 명                       | 기능                                                         | 사용 예                                                  |
| ----------------------------- | ------------------------------------------------------------ | -------------------------------------------------------- |
| ASCII( char )                 | char 문자의 ASCII 코드 값을 반환,<br />CHR 함수와 반대 기능을 함 | SELECT ASCII('A')<br />FROM DAUL;<br />=> 65             |
| INSTR( char1, char2, n1, n2 ) | char1에서 char2 문자를 찾아 시작 위치를 반환<br />n1은 char1에서 몇 번째 문자부터 찾을 것인지를 나타내는 위치이며 생략 시 1이 적용<br />n2는 char1에서 char2 문자를 찾을 때 일치하는 문자의 몇 번째 위치를 반환할지를 나타내며 생략 시 1이 적용 | SELECT INSTR('ABABAB', 'A', 2)<br />FROM DAUL;<br />=> 3 |
| LENGTH( char )                | char 문자의 글자 수를 반환                                   | SELECT LENGTH('the')<br />FROM DAUL;<br />=> 3           |

<br>

<br>

### 3. 날짜형 함수

<br>

| 함수 명                       | 기능                                                         | 사용 예                                                      |
| ----------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| SYSDATE                       | 현재 일자와 시간을 반환                                      | SELECT SYSDATE<br />FROM DAUL;<br />=> 2021-03-30            |
| ADD_MONTHS( date, n )         | date 날짜에 n개월을 더한 날짜를 반환<br />n이 음수면 더하지 않고 뺀 날짜를 반환 | SELECT ADD_MONTHS(SYSDATE, 1)<br />FROM DAUL;<br />=> 2021-04-30 |
| MONTHS_BETWEEN( date1, date2) | date1과 date2 두 날짜 사이의 개월 수를 반환,<br />date1이 date2보다 이후 날짜면 양수, 반대면 음수 반환 | SELECT MONTHS_BETWEEN(SYSDATE+31, SYSDATE)<br />FROM DAUL;<br />=> 1.096... |
| LAST_DAY( date )              | date가 속한 월의 마지막 일자를 반환                          | SELECT LAST_DAY(SYSDATE)<br />FROM DAUL;<br />=> 2019-03-31  |
| NEXT_DAY( date, expr )        | date 날짜를 기준으로 expr에 명시한 날짜 반환,<br />expr은 요일을 나타내는데 '월요일' 형태로 쓸 수도 있고 1~7(일~토)까지 숫자를 쓸 수도 있다 | SELECT NEXT_DAY(SYSDATE, '월요일')<br />FROM DAUL;<br />=> 2021-04-05 |
| ROUND( date, format )         | date를 format 기준으로 반올림한 날짜 반환,<br />format은 YEAR, MONTH, DD, HH, HH24, MI 등 사용 가능 | SELECT ROUND(SYSDATE, 'YEAR')<br />FROM DAUL;<br />=> 2021-01-01 |
| TRUNC( date, format )         | date를 format 기준으로 잘라낸 날짜 반환,<br />format은 ROUND함수와 동일하게 사용 가능 | SELECT TRUNC(SYSDATE, 'YEAR')<br />FROM DAUL;<br />=> 2021-01-01 |

<br>

<br>

### 4. 형변환 함수

<br>

| 함수 명                     | 기능                                                         | 사용 예                                                      |
| --------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| TO_NUMBER( char )           | char을 숫자로 변환                                           | SELECT TO_NUMBER('12345')<br />FROM DAUL;<br />=> 12345      |
| TO_CHAR( n, number_format)  | 숫자인 n을 number_format에 맞게 문자로 변환,<br />number_format은 생략 가능 | SELECT TO_CHAR(12345, '99,999'<br />FROM DAUL;<br />=> '12,345' |
| TO_CHAR( date, date_format) | 날짜인 date를 date_format에 맞게 문자로 변환,<br />date_format은 생략 가능 | SELECT TO_CHAR(SYSDATE, 'YYYY-MM-DD HH24:MI:SS')<br />FROM DAUL;<br />=> '2021-03-30 15:41:01' |
| TO_DATE( char, date_format) | 문자 char을 date_format에 맞게 날짜로 변환,<br />date_format은 생략 가능 | SELECT TO_CHAR('2021-03-30 15:41:01', 'YYYY-MM-DD HH24:MI:SS')<br />FROM DAUL;<br />=> 2021-03-30 15:41:01 |

<br>

| 형식             | 설명                              |
| ---------------- | --------------------------------- |
| YYYY, YYY, YY, Y | 연도 표시                         |
| MONTH, MON       | 월 표시                           |
| MM               | 월을 01, 02,,,, 12 형태로 표현    |
| D                | 주중 일자를 1~7까지 숫자로 표현   |
| DAY              | 주중 일자를 요일로 표현           |
| DD               | 일을 01, 02,,,, 31 형태로 표현    |
| DDD              | 일을 001, 002,,,, 365 형태로 표현 |
| DL               | 일을 요일까지 표현                |
| HH, HH12         | 시간을 01, 02,,,, 12 형태로 표현  |
| HH24             | 시간을 01, 02,,,, 24 형태로 표현  |
| MI               | 분을 01, 02,,,, 59 형태로 표현    |
| SS               | 초를 01, 02,,,, 59 형태로 표현    |
| WW               | 주를 01, 02,,,, 53 형태로 표현    |

<br>

<br>

## 6.3 기타 함수

<br>

<br>

### 1. NULL 관련 함수

<br>

| 함수 명                      | 사용                                                         | 기능 예                                                      |
| ---------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| NVL( expr1, expr2 )          | expr1 값이 NULL인 경우 expr2를 반환, 아닌 경우 expr1 반환    | SELECT NVL(NULL, 'N/A')<br />FROM DAUL;<br />=> N/A          |
| NVL2( expr1, expr2, expr3 )  | expr1값이 NULL인 경우 expr3을, NULL이 아닌 경우에는 expr2를 반환 | SELECT NVL2(1, 2, 3)<br />FROM DAUL;<br />=> 2               |
| COALESCE( expr1, expr2, ...) | expr1, expr2, ...에서 첫 번째로 NULL 값이 아닌 값을 반환     | SELECT COALESCE(NULL, NULL, 5, 4, NULL)<br />FROM DAUL;<br />=> 5 |
| NULLIF( expr1, expr2)        | expr1과 expr2 값을 비교해 두 값이 같으면 NULL을, 같지 않으면 expr1을 반환 | SELECT NULLIF('NULL', 'null')<br />FROM DAUL;<br />=> NULL   |

<br>

<br>

### 2. 기타 함수

<br>

- GREATEST( expr1, expr2, ....) : 매개변수 중 가장 큰 값을 반환 (문자형 > 숫자형)
- LEAST( expr1, expr2, ....) : 매개변수 중 가장 작은 값을 반환
- DECODE( expr, comp_val1, result1, compval2, result2, ..., default_value) : expr 값이 comp_val1과 같으면 result1을 반환하고, comp_val2와 같으면 result2를 반환하는 함수, 어느 것과 같지 않다면 default_value를 반환하는데 명시되지 않았다면 NULL을 반환

<br>

<br>

## 6.4 CASE 표현식

<br>

- CASE 표현식이 DECODE 함수와 동작 방식이 유사하다

<br>

``` mysql
# 단순형 CASE 표현식 구문
CASE	expr	WHEN comparision_expr1 THEN return_expr1
				WHEN comparision_expr2 THEN	return_expr2
				....
				ELSE else_expr
END


# 검색형 CASE 표현식 구문
CASE	WHEN condition1	THEN return_expr1
		WHEN condition2 THEN return_expr2
		....
		ELSE else_expr
END
```

<br>

``` mysql
# 검색형 CASE 표현식
SELECT	emp_name
		,age
		,CASE	WHEN	age BETWEEN 0 AND 19	THEN '10대'
				WHEN	age BETWEEN 20 AND 29	THEN '20대'
				WHEN	age BETWEEN 30 AND 39	THEN '30대'
				WHEN	age BETWEEN 40 AND 49	THEN '40대'
				WHEN	age BETWEEN 50 AND 59	THEN '0대'
				ELSE '60대 이상'
		END ages
	FROM EMP03;
```

<br>
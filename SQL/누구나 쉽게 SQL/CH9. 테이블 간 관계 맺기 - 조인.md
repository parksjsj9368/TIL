# CH9. 테이블 간 관계 맺기 - 조인

<br>

<br>

## 9.1 조인이란?

<br>

- RDBMS의 특징 : 테이블을 분리하여 데이터의 중복 저장을 피하고 테이블 간 관계를 맺어 원하는 정보를 가져오는 것

  => 관계를 맺는것 : 조인

<br>

- 조인을 하기 위해서는 두 테이블 간 연결고리 할 컬럼이 있어야한다

1. 컬럼 이름은 다르게 사용하기도 하지만 대게 이름 같게 한다
2. 데이터형은 무조건 같아야 한다

<br>

<br>

## 9.2 내부 조인

<br>

<br>

### ORACLE 기본 구문 : WHERE절 사용

<br>

- 내부 조인 : WHERE 절에서 동등 연산자를 사용해 연결고리 컬럼을 비교하는 조인

<br>

``` mysql
# 내부 조인
SELECT	a.emp_id, a.emp_name, a.gender, a.age, a.dept_id, 
		b.dept_id, b.dept_name, b.use_yn
	FROM	emp_master a
			,dept_master b
WHERE	a.dept_id == b.dept_id
ORDER BY	a.emp_id;
```

- SELECT 절에서 dept_id라는 동일한 컬럼을 2번 불러오는데 알아서 하나는 dept_id_1로 바꿔준다

<br>

<br>

### ANSI 구문 : INNER JOIN

<br>

``` mysql
# ANSI 구문으로 작성한 내부 조인
SELECT	a.emp_id, a.emp_name, a.gender, a.age, a.dept_id, 
		b.dept_id, b.dept_name, b.use_yn
	FROM	emp_master a
INNER JOIN	dept_master b
	ON		a.dept_id == b.dept_id
ORDER BY	a.emp_id;
```

- ANSI 내부 조인은 INNER JOIN 다음에 조인할 테이블을 명시하고 조인 컬럼 조건을 ON절에 기술

<br>

<br>

``` mysql
# 내부 조인에서 남성만 조회 한 경우

## 기본 구문
SELECT	a.emp_id, a.emp_name, a.gender, a.age, a.dept_id, 
		b.dept_id, b.dept_name, b.use_yn
	FROM	emp_master a
			,dept_master b
WHERE	a.dept_id == b.dept_id
	AND		a.gender = '남성'
ORDER BY	a.emp_id;


## ANSI 구문
SELECT	a.emp_id, a.emp_name, a.gender, a.age, a.dept_id, 
		b.dept_id, b.dept_name, b.use_yn
	FROM	emp_master a
INNER JOIN	dept_master b
	ON		a.dept_id == b.dept_id
WHERE		a.gender = '남성'
ORDER BY	a.emp_id;
```

<br>

<br>

## 9.3 외부 조인

<br>

<br>

### ORACLE 기본 구문 : WHERE절과 (+) 사용

- 외부 조인 : 두 테이블 중 한 테이블의 조인 컬럼 값이 없더라도 없는 건까지 모두 포함해 조회하는 조인

<br>

```mysql
# 외부 조인
SELECT	a.emp_id, a.emp_name, a.gender, a.age, a.dept_id, 
		b.dept_id, b.dept_name, b.use_yn
	FROM	emp_master a
			,dept_master b
WHERE	a.dept_id == b.dept_id (+)
ORDER BY	a.emp_id;
```

- 두 테이블에서 데이터를 모두 가져올 기준 테이블(emp_master) 반대에 (+)를 붙여준다

<br>

<br>

### ANSI 구문 : LEFT JOIN, RIGHT JOIN, FULL OUTER JOIN

<br>

``` mysql
# ANSI 구문으로 작성한 외부 조인

# LEFT JOIN : 기준 컬럼이 왼쪽 (사원 테이블)
SELECT	a.emp_id, a.emp_name, a.gender, a.age, a.dept_id, 
		b.dept_id, b.dept_name, b.use_yn
	FROM	emp_master a
LEFT (OUTER) JOIN	dept_master b
	ON		a.dept_id == b.dept_id
ORDER BY	a.emp_id;


# RIGHT JOIN : 기준 컬럼이 오른쪽 (부서 테이블) 
SELECT	a.emp_id, a.emp_name, a.gender, a.age, a.dept_id, 
		b.dept_id, b.dept_name, b.use_yn
	FROM	emp_master a
RIGHT (OUTER) JOIN	dept_master b
	ON		a.dept_id == b.dept_id
ORDER BY	a.emp_id;


# FULL OUTER JOIN : 두 테이블의 데이터를 모두 조회
SELECT	a.emp_id, a.emp_name, a.gender, a.age, a.dept_id, 
		b.dept_id, b.dept_name, b.use_yn
	FROM	emp_master a
FULL OUTER JOIN	dept_master b
	ON		a.dept_id == b.dept_id
ORDER BY	a.emp_id;
```

<br>

<br>

## 9.4 카디션 곱

<br>

- 카디션 곱 : WHERE 절에 조인 조건을 주지 않는 조인

<br>

``` MYSQL
# 카디션 곱
SELECT	a.emp_id, a.emp_name, a.gender, a.age, a.dept_id, 
		b.dept_id, b.dept_name, b.use_yn
	FROM	emp_master a
			,dept_master b
ORDER BY	a.emp_id;
```

- 사원 테이블의 총 로우 수 : 6개,	부서 테이블의 총 로우 5개
- 두 테이블을 조인하되 조인 조건을 주지 않으므로 가능한 모든 조합에 대한 데이터가 조회 된다
- 그 결과, 6*5 = 30건이 조회

<br>
### [SELECT]

<br>

1. 모든 레코드 조회하기

문제 : 동물 보호소에 들어온 모든 동물의 정보를 ANIMAL_ID 순으로 조회하는 SQL 문을 작성해주세요.

```MYSQL
SELECT *
FROM ANIMAL_INS
ORDER BY ANIMAL_ID ASC;
```

<br>

2. 역순 정렬하기

문제 : 동물 보호소에 들어온 모든 동물의 이름과 보호 시작일을 조회하는 SQL 문을 작성해주세요. 이때 결과는 ANIMAL_ID 역순으로 보여주세요.

```MYSQL
SELECT NAME, DATETIME
FROM ANIMAL_INS
ORDER BY ANIMAL_ID DESC;
```

<br>

3. 아픈 동물 찾기

문제 : 동물 보호소에 들어온 동물 중 아픈 동물의 아이디와 이름을 조회하는 SQL 문을 작성해주세요. 이때 결과는 ANIMAL_ID 순으로 보여주세요.

```MYSQL
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE INTAKE_CONDITION = 'Sick'
ORDER BY ANIMAL_ID ASC;
```

<br>

4. 어린 동물 찾기

문제 : 동물 보호소에 들어온 동물 중 젊은 동물의 아이디와 이름을 조회하는 SQL 문을 작성해주세요. 이때 결과는 ANIMAL_ID 순으로 보여주세요.

```MYSQL
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE INTAKE_CONDITION != 'Aged'
ORDER BY ANIMAL_ID;
```

<br>

5. 동물의 아이디와 이름

문제 : 동물 보호소에 들어온 모든 동물의 아이디와 이름을 ANIMMAL_ID 순으로 조회하는 SQL 문을 작성해주세요.

```MYSQL
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
ORDER BY ANIMAL_ID;
```

<br>

6. 여러 기준으로 정렬하기

문제 : 동물 보호소에 들어온 모든 동물의 아이디와 이름, 보호 시작일을 이름 순으로 조회하는 SQL 문을 작성해주세요. 단, 이름이 같은 동물 중에서는 보호를 나중에 시작한 동물을 먼저 보여줘야 합니다.

```MYSQL
SELECT ANIMAL_ID, NAME, DATETIME
FROM ANIMAL_INS
ORDER BY NAME, DATETIME DESC;
```

<br>

7. 상위 n개 레코드

문제 : 동물 보호소에 가장 먼저 들어온 동물의 이름을 조회하는 SQL 문을 작성해주세요.

```MYSQL
SELECT NAME
FROM ANIMAL_INS
ORDER BY DATETIME
LIMIT 1;
```

<br>

<br>

### [SUM, MAX, MIN]

<br>

1. 최댓값 구하기

문제 : 가장 최근에 들어온 동물은 언제 들어왔는지 조회하는 SQL 문을 작성해주세요.

```MYSQL
SELECT DATETIME AS 시간
FROM ANIMAL_INS
ORDER BY DATETIME DESC
LIMIT 1;

SELECT MAX(DATETIME) AS 시간
FROM ANIMAL_INS;
```

<br>

2. 최솟값 구하기

문제 : 동물 보호소에 가장 먼저 들어온 동물은 언제 들어왔는지 조회하는 SQL문을 작성해주세요.

```MYSQL
SELECT DATETIME AS 시간
FROM ANIMAL_INS
ORDER BY DATETIME
LIMIT 1;

SELECT MIN(DATETIME) AS 시간
FROM ANIMAL_INS;
```

<br>

3. 동물 수 구하기

문제 : 동물 보호소에 동물이 몇 마리 들어왔는지 조회하는 SQL 문을 작성해주세요.

```MYSQL
SELECT COUNT(*)
FROM ANIMAL_INS;
```

<br>

4. 중복 제거하기

문제 : 동물 보호소에 들어온 동물의 이름은 몇 개 인지 조회하는 SQL 문을 작성해주세요. 이때 이름이 NULL인 경우는 집계하지 않으며 중복되는 이름은 하나로 칩니다.

```MYSQL
SELECT COUNT(DISTINCT NAME)
FROM ANIMAL_INS
WHERE NAME IS NOT NULL;

SELECT COUNT(*)
FROM (
    SELECT DISTINCT NAME
    FROM ANIMAL_INS
    WHERE NAME IS NOT NULL
) DATA;
```

<br>

<br>

### [GROUP BY]

<br>

1. 고양이와 개는 몇 마리 있을까

문제 : 동물 보호소에 들어온 동물 중 고양이와 개가 각각 몇 마리인지 조회하는 SQL 문을 작성해주세요. 이때 고양이를 개보다 먼저 조회해주세요.

```MYSQL
SELECT ANIMAL_TYPE, COUNT(ANIMAL_TYPE) AS count
FROM ANIMAL_INS
WHERE ANIMAL_TYPE IN ('Cat', 'Dog')
GROUP BY ANIMAL_TYPE
ORDER BY ANIMAL_TYPE;
```

<br>

2. 동명 동물 수 찾기

문제 : 동물 보호소에 들어온 동물 이름 중 두 번 이상 쓰인 이름과 해당 이름이 쓰인 횟수를 조회하는 SQL 문을 작성해주세요. 이때 결과는 이름이 없는 동물은 집계에서 제외하며 결과는 이름 순으로 조회해주세요.

```MYSQL
SELECT NAME, COUNT(NAME) AS COUNT
FROM ANIMAL_INS
WHERE NAME IS NOT NULL
GROUP BY NAME
HAVING COUNT(NAME) >= 2
ORDER BY NAME;
```

<br>

3. 입양 시각 구하기(1)

문제 : 보호소에서는 몇 시에 입양이 가장 활발하게 일어나는지 알아보려 합니다. 09:00부터 19:59까지, 각 시간대별로 입양이 몇 건이나 발생했는지 조회하는 SQL 문을 작성해주세요. 이때 결과는 시간대 순으로 정렬해야 합니다.

```MYSQL
SELECT HOUR(DATETIME) AS HOUR, COUNT(*) AS COUNT
FROM ANIMAL_OUTS
WHERE HOUR(DATETIME) >= 9
    AND HOUR(DATETIME) <= 19
GROUP BY HOUR(DATETIME)
ORDER BY 1;
```

<br>

4. 입양 시각 구하기(2)

문제 : 보호소에서는 몇 시에 입양이 가장 활발하게 일어나는지 알아보려 합니다. 0시부터 23시까지, 각 시간대별로 입양이 몇 건이나 발생했는지 조회하는 SQL 문을 작성해주세요. 이때 결과는 시간대 순으로 정렬해야 합니다.

```MYSQL
SET @hour := -1; -- 변수 선언
SELECT	(@hour := @hour + 1) AS HOUR,
		(SELECT COUNT(*) 
		 FROM ANIMAL_OUTS 
		 WHERE HOUR(DATETIME) = @hour) AS COUNT
FROM ANIMAL_OUTS
WHERE @hour < 23;
```

<br>

<br>

### [IS NULL]

<br>

1. 이름이 없는 동물의 아이디

문제 : 동물 보호소에 들어온 동물 중, 이름이 없는 채로 들어온 동물의 ID를 조회하는 SQL 문을 작성해주세요. 단, ID는 오름차순 정렬되어야 합니다.

```MYSQL
SELECT ANIMAL_ID
FROM ANIMAL_INS
WHERE NAME IS NULL
ORDER BY ANIMAL_ID;
```

<br>

2. 이름이 있는 동물의 아이디

문제 : 동물 보호소에 들어온 동물 중, 이름이 있는 동물의 ID를 조회하는 SQL 문을 작성해주세요. 단, ID는 오름차순 정렬되어야 합니다.

```MYSQL
SELECT ANIMAL_ID
FROM ANIMAL_INS
WHERE NAME IS NOT NULL
ORDER BY ANIMAL_ID;
```

<br>

3. NULL 처리하기

문제 : 동물의 생물 종, 이름, 성별, 및 중성화 여부를 아이디 순으로 조회하는 SQL 문을 작성해주세요. 이때 프로그래밍을 모르는 사람들은 NULL이라는 기호를 모르기 때문에, 이름이 없는 동물의 이름은 "No name"으로 표시해주세요.

```MYSQL
-- MYSQL에는 NVL이 없기에 IFNULL 사용한다
SELECT ANIMAL_TYPE, IFNULL(NAME, 'No name'), SEX_UPON_INTAKE
FROM ANIMAL_INS
ORDER BY ANIMAL_ID;
```

<br>

<br>

### [JOIN]

<br>

1. 없어진 기록 찾기

문제 : 천재지변으로 인해 일부 데이터가 유실되었습니다. 입양을 간 기록은 있는데 보호소에 들어온 기록이 없는 동물의 ID와 이름을 ID 순으로 조회하는 SQL 문을 작성해주세요.

```MYSQL
SELECT B.ANIMAL_ID, B.NAME
FROM ANIMAL_INS A
RIGHT OUTER JOIN ANIMAL_OUTS B 
    USING (ANIMAL_ID)
WHERE INTAKE_CONDITION IS NULL
ORDER BY 1;
```

<br>

2. 있었는데요 없었습니다

문제 : 관리자의 실수로 일부 동물의 입양일이 잘못 입력되었습니다. 보호 시작일보다 입양일이 더 빠른 동물의 아이디와 이름을 조회하는 SQL 문을 작성해주세요. 이때 결과는 보호 시작일이 빠른 순으로 조회해야합니다.

```MYSQL
SELECT B.ANIMAL_ID, B.NAME
FROM ANIMAL_INS A
INNER JOIN ANIMAL_OUTS B
    USING (ANIMAL_ID)
WHERE A.DATETIME > B.DATETIME
ORDER BY A.DATETIME;
```

<br>

3. 오랜 기간 보호한 동물(1)

문제 : 아직 입양을 못 간 동물 중, 가장 오래 보호소에 있었던 동물 3마리의 이름과 보호 시작일을 조회하는 SQL 문을 작성해주세요. 이때 결과는 보호 시작일 순으로 조회해야 합니다.

```MYSQL
SELECT A.NAME, A.DATETIME
FROM ANIMAL_INS A
LEFT JOIN ANIMAL_OUTS B
    USING (ANIMAL_ID)
WHERE B.DATETIME IS NULL
ORDER BY 2
LIMIT 3;
```

<br>

4. 보호소에서 중성화한 동물

문제 : 보호소에 들어올 당시에는 중성화되지 않았지만, 보호소를 나갈 당시에는 중성화된 동물의 아이디와 생물 종, 이름을 조회하는 아이디 순으로 조회하는 SQL 문을 작성해주세요.

```MYSQL
SELECT A.ANIMAL_ID, A.ANIMAL_TYPE, A.NAME
FROM ANIMAL_INS A
INNER JOIN ANIMAL_OUTS B
    USING (ANIMAL_ID)
WHERE A.SEX_UPON_INTAKE LIKE 'Intact%' -- %는 모든것을 의미
    AND B.SEX_UPON_OUTCOME NOT LIKE 'Intact%'
ORDER BY 1;
```

<br>

<br>

### [String, Date]

<br>

1. 루시와 엘라 찾기

문제 : 동물 보호소에 들어온 동물 중 이름이 Lucy, Ella, Pickle, Rogan, Sabrina, Mitty인 동물의 아이디와 이름, 성별 및 중성화 여부를 조회하는 SQL 문을 작성해주세요.

```MYSQL
SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS
WHERE NAME IN ('Lucy','Ella','Pickle','Rogan','Sabrina','Mitty');
```

<br>

2. 이름에 el이 들어가는 동물 찾기

문제 : 동물 보호소에 들어온 동물 이름 중, 이름에 'EL'이 들어가는 개의 아이디와 이름을 조회하는 SQL 문을 작성해주세요. 이때 결과는 이름 순으로 조회해주세요. 단, 이름의 대소문자는 구분하지 않습니다.

```MYSQL
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE ANIMAL_TYPE = 'Dog'
    AND NAME LIKE '%EL%'
-- MYSQL은 대소문자를 구분하지 않는다
ORDER BY NAME;
```

<br>

3. 중성화 여부 파악하기

문제 : 중성화된 동물은 SEX_UPON_INTAKE 컬럼에 'Neutered' 또는 'Spayed'라는 단어가 들어있습니다. 동물의 아이디와 이름, 중성화 여부를 아이디 순으로 조회하는 SQL 문을 작성해주세요. 이때 중성화가 되어 있다면 'O', 아니라면 'X'라고 표시해주세요.

```MYSQL
SELECT  ANIMAL_ID, NAME
        , CASE  WHEN SEX_UPON_INTAKE LIKE 'Neutered%'	THEN 'O'
                WHEN SEX_UPON_INTAKE LIKE 'Spayed%'     THEN 'O'
                ELSE 'X'
        END 중성화
FROM ANIMAL_INS
ORDER BY ANIMAL_ID;
```

<br>

4. 오랜 기간 보호한 동물(2)

문제 : 입양을 간 동물 중, 보호 기간이 가장 길었던 동물 두마리의 아이디와 이름을 조회하는 SQL 문을 작성해주세요. 이때 결과는 보호 기간이 긴 순으로 조회해야 합니다.

```MYSQL
SELECT B.ANIMAL_ID, B.NAME
FROM ANIMAL_INS A
RIGHT OUTER JOIN ANIMAL_OUTS B
    USING (ANIMAL_ID)
ORDER BY DATEDIFF(B.DATETIME, A.DATETIME) DESC
LIMIT 2;
-- MYSQL에는 MONTHS_BETWEEN이 없기에 DATEDIFF 사용한다

-- [ORACLE]
SELECT B.ANIMAL_ID, B.NAME
FROM ANIMAL_INS A
RIGHT OUTER JOIN ANIMAL_OUTS B
    USING (ANIMAL_ID)
ORDER BY MONTHS_BETWEEN(B.DATETIME, A.DATETIME) DESC
LIMIT 2;
```

<br>

5. DATETIME에서 DATE로 형 변환

문제 : 테이블에 등록된 모든 레코드에 대해, 각 동물의 아이디와 이름, 들어온 날짜를 조회하는 SQL 문을 작성해주세요. 이때 결과는 아이디 순으로 조회해야 합니다.

```MYSQL
SELECT  ANIMAL_ID, NAME
        , DATE_FORMAT(DATETIME, '%Y-%m-%d') AS 날짜
FROM ANIMAL_INS
ORDER BY ANIMAL_ID;
-- MYSQL에는 TO_CHAR이 없기에 DATE_FORMAT 사용한다

-- [ORACLE]
SELECT  ANIMAL_ID, NAME
        , TO_CHAR(DATETIME, 'YYYY-MM-DD') AS 날짜
FROM ANIMAL_INS
ORDER BY ANIMAL_ID;
```

<br>

<br>

### [Summer/Winter Coding(2019)]

<br>

1. 우유와 요거트가 담긴 장바구니

문제 : 우유와 요거트를 동시에 구입한 장바구니의 아이디를 조회하는 SQL 문을 작성해주세요. 이때 결과는 장바구니의 아이디 순으로 나와야 합니다.

```MYSQL
SELECT DISTINCT(CART_ID)
FROM CART_PRODUCTS
WHERE NAME = 'Milk'
    AND CART_ID IN (
        SELECT CART_ID
        FROM CART_PRODUCTS
        WHERE NAME = 'Yogurt'
    )
ORDER BY CART_ID;
```

<br>

<br>

### [2021 Dev-Matching]

<br>

1. 헤비 유저가 소유한 장소

문제 : 이 서비스에서는 공간을 둘 이상 등록한 사람을 헤비 유저 라고 부릅니다. 헤비 유저가 등록한 공간의 정보를 아이디 순으로 조회하는 SQL 문을 작성해주세요.

``` MYSQL
SELECT *
FROM PLACES 
WHERE HOST_ID IN (
    SELECT A.HOST_ID
    FROM PLACES A
    GROUP BY A.HOST_ID
    HAVING COUNT(A.HOST_ID) >= 2
    )
ORDER BY ID;
```

<br>
-- 코드를 입력하세요
SELECT
    A.ANIMAL_ID,
    A.ANIMAL_TYPE,
    A.NAME
FROM
    ANIMAL_OUTS A
INNER JOIN
    (
        SELECT 
            ANIMAL_ID
        FROM 
            ANIMAL_INS
        WHERE 
            SEX_UPON_INTAKE NOT LIKE 'Spayed%' 
            AND SEX_UPON_INTAKE NOT LIKE 'Neutered%'
    ) B ON A.ANIMAL_ID=B.ANIMAL_ID
WHERE
    A.SEX_UPON_OUTCOME LIKE 'Spayed%' 
    OR A.SEX_UPON_OUTCOME LIKE 'Neutered%'

     
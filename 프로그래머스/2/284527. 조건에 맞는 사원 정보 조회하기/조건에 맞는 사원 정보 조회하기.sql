-- 코드를 작성해주세요
SELECT
    B.SCORE,
    B.EMP_NO,
    A.EMP_NAME,
    A.POSITION,
    A.EMAIL
FROM
    HR_EMPLOYEES A
INNER JOIN
    (
        SELECT
            EMP_NO,
            SUM(SCORE) SCORE
        FROM 
            HR_GRADE 
        WHERE
            YEAR=2022
        GROUP BY
            EMP_NO
        ORDER BY
            SCORE DESC
        LIMIT 1
    ) B ON A.EMP_NO=B.EMP_NO

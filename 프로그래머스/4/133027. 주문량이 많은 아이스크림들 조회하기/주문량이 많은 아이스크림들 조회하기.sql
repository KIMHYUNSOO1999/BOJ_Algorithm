-- 코드를 입력하세요
SELECT
    A.FLAVOR
FROM 
    (
    SELECT
        FLAVOR,
        SUM(TOTAL_ORDER) AS TMP_SUM
    FROM
        JULY 
    GROUP BY
        FLAVOR

    UNION

    SELECT
        FLAVOR,
        SUM(TOTAL_ORDER) AS TMP_SUM
    FROM
        FIRST_HALF 
    GROUP BY
        FLAVOR
    ) A
GROUP BY
    A.FLAVOR
ORDER BY
    SUM(TMP_SUM) DESC
LIMIT 3;
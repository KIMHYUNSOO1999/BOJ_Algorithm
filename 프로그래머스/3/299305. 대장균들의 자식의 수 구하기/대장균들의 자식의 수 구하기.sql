-- 코드를 작성해주세요
SELECT
    A.ID,
    IFNULL(B.CHILD_COUNT,0) CHILD_COUNT
FROM
    ECOLI_DATA A
LEFT JOIN
    (
        SELECT
            PARENT_ID ID,
            COUNT(*) CHILD_COUNT
        FROM
            ECOLI_DATA
        GROUP BY
            PARENT_ID
    ) B ON A.ID= B.ID
ORDER BY
    A.ID ASC

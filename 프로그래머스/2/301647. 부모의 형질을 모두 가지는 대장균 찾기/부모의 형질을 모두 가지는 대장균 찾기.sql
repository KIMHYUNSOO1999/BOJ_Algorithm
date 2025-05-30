-- 코드를 작성해주세요
SELECT
    A.ID,
    A.GENOTYPE,
    B.GENOTYPE PARENT_GENOTYPE
FROM
    ECOLI_DATA A
INNER JOIN
    ECOLI_DATA B ON A.PARENT_ID=B.ID
WHERE
    B.GENOTYPE & A.GENOTYPE = B.GENOTYPE
ORDER BY
    A.ID
-- 코드를 작성해주세요
SELECT
    COUNT(*) FISH_COUNT
FROM 
    FISH_INFO A
INNER JOIN
    (
        SELECT
            FISH_TYPE
        FROM
            FISH_NAME_INFO
        WHERE
            FISH_NAME IN ('BASS','SNAPPER')
    ) B ON A.FISH_TYPE=B.FISH_TYPE
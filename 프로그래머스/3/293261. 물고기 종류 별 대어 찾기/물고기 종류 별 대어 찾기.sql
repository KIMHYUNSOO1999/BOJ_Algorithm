-- 코드를 작성해주세요
SELECT 
    A.ID, 
    C.FISH_NAME, 
    A.LENGTH
FROM 
    FISH_INFO A
INNER JOIN 
    (
        SELECT 
            FISH_TYPE, 
            MAX(LENGTH) AS MAX_LENGTH
        FROM 
            FISH_INFO
        GROUP BY 
            FISH_TYPE
    ) B ON A.FISH_TYPE = B.FISH_TYPE AND A.LENGTH = B.MAX_LENGTH
INNER JOIN 
    FISH_NAME_INFO C ON A.FISH_TYPE = C.FISH_TYPE
ORDER BY 
    A.ID ASC;



-- 코드를 작성해주세요
SELECT 
    A.ITEM_ID,
    B.ITEM_NAME,
    B.RARITY
FROM 
    ITEM_TREE A
INNER JOIN
    ITEM_INFO B ON A.ITEM_ID = B.ITEM_ID
WHERE 
    NOT EXISTS (
        SELECT 
            1
        FROM 
            ITEM_TREE C
        WHERE 
            C.PARENT_ITEM_ID = A.ITEM_ID
    )
ORDER BY
    A.ITEM_ID DESC;
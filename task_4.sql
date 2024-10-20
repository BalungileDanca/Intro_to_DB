SELECT 
    COLUMN_NAME AS Field,
    COLUMN_TYPE AS Type,
    IS_NULLABLE AS IS_NULLABLE,
    COLUMN_KEY AS COLUMN_KEY,
    COLUMN_DEFAULT AS DefaultValue,
    EXTRA AS Extra
FROM 
    INFORMATION_SCHEMA.COLUMNS
WHERE 
    TABLE_SCHEMA = 'alx_book_store' -- This will use the database passed as an argument
    AND TABLE_NAME = 'books';

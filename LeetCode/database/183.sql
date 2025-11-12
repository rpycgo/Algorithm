SELECT
    name AS Customers
FROM
    Customers a
WHERE
    NOT EXISTS (
        SELECT 1
        FROM Orders b
        WHERE b.customerId = a.id
    );

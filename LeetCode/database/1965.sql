SELECT
    employee_id
FROM (
    SELECT
        e.employee_id, e.name, s.salary
    FROM
        Employees e
    LEFT JOIN
        Salaries s
    USING
        (employee_id)

    UNION

    SELECT
        s.employee_id, e.name, s.salary
    FROM
        Salaries s
    LEFT JOIN
        Employees e
    USING (employee_id)
) AS t
WHERE
    name IS NULL OR salary IS NULL
ORDER BY
    employee_id

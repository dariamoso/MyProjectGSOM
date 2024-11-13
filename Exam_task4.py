%%sql postgresql:///jovyan
SELECT 
    d.department_name,
    (SELECT e.last_name
     FROM Employees e 
     WHERE e.employee_id = d.manager_id) AS Manager,
    (SELECT COUNT(*) 
     FROM Employees e 
     WHERE e.department_id = d.department_id) AS Employees_number
FROM Departments d
ORDER BY d.department_name;
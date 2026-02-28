/* Write your PL/SQL query statement below */
select e.employee_id from Employees e
where e.salary < 30000
and e.manager_id not in(select e2.employee_id from Employees e2)
order by e.employee_id asc
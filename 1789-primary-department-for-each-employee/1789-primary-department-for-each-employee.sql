# Write your MySQL query statement below

select distinct employee_id, department_id from (
select * from employee a
union
select employee_id, department_id, 'Y' primary_flag from employee
          group by employee_id having Count(*) = 1
) k where primary_flag = 'Y'

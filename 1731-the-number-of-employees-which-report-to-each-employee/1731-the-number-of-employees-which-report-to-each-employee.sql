# Write your MySQL query statement below


select a.employee_id, a.name, count(*) reports_count, round(avg(b.age),0) average_age
    from employees a
inner join employees b
on a.employee_id = b.reports_to
group by 1, 2
order by 1
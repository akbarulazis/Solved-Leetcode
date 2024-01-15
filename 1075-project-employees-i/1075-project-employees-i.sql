# Write your MySQL query statement below
select project_id,
round(avg(experience_years),2) average_years
    from project a
left join employee b
on a.employee_id = b.employee_id
group by 1
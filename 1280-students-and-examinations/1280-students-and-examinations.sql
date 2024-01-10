# Write your MySQL query statement below
select 
a.student_id, a.student_name, b.subject_name,
sum(case when c.subject_name is not null then 1 else 0 end) attended_exams
from students a
cross join subjects b
left join examinations c
on a.student_id = c.student_id
and b.subject_name = c.subject_name
group by 1,2,3
order by 1,2
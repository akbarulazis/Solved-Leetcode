# Write your MySQL query statement below

select id, case when name_swap is null then student else name_swap end student from (
select *, 
case when id%2 = 1 then lead(student,1,null) over(order by id)
else lag(student,1,null) over(order by id) end name_swap
from seat ) k
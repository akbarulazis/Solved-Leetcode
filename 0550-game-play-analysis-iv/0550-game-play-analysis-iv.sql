# Write your MySQL query statement below

select round(sum(if (datediff(maxd,md) = 1 , 1 , 0) ) / count(distinct player_id),2) fraction from (
select  
player_id, min(event_date) md, max(event_date) maxd
from (
select *, row_number() over(partition by player_id order by event_date asc) row_num
from activity )
k

where row_num in (1,2)
group by 1 ) k

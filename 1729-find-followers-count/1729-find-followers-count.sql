# Write your MySQL query statement below

select user_id, count(1) followers_count
from followers
group by 1 order by 1
# Write your MySQL query statement below
SELECT a.user_id , round(sum( case when c.action is not null and action = 'confirmed'
then 1 else 0 end) / count(*),2) confirmation_rate
FROM SIGNUPS a
left join confirmations c
on a.user_id = c.user_id
group by 1
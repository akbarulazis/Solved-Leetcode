# Write your MySQL query statement below
SELECT a.user_id , round(avg(if(c.action = 'confirmed',1,0)),2) confirmation_rate
FROM SIGNUPS a
left join confirmations c
on a.user_id = c.user_id
group by 1
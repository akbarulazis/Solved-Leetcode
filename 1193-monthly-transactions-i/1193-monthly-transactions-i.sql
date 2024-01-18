# Write your MySQL query statement below
select date_format(trans_date, '%Y-%m') month, country, count(1) trans_count
, sum(case when state = 'approved' then 1 else 0 end) approved_count, 
sum(amount) trans_total_amount
, sum(case when state = 'approved' then amount else 0 end) approved_total_amount
from transactions
group by 1,2
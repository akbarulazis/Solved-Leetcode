# Write your MySQL query statement below

select round(sum( case when first_order = delivery_date then 1 else 0 end)*100 / count(*) ,2) immediate_percentage from (
select customer_id, min(order_date) first_order, min(customer_pref_delivery_date) delivery_date
from delivery 
group by 1 ) k
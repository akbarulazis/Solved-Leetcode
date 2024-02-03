# Write your MySQL query statement below

select customer_id from customer a
group by customer_id
having count(distinct product_key) = (select count(*) from product)
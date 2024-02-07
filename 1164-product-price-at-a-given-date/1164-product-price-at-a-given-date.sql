# Write your MySQL query statement below

select a.product_id, coalesce(new_price,10) price
from (
select distinct product_id from products) a
left join (
select a.product_id, new_price
from products a
left join (
select product_id, max(change_date) mx_date from products
    where change_date <= '2019-08-16'
    group by 1
) b
on a.product_id =  b.product_id and a.change_date = b.mx_date
where mx_date is not null 
) b
on a.product_id =  b.product_id

# Write your MySQL query statement below
select product_id, coalesce(round(sum(pu)/sum(units),2),0) average_price from (
select a.*, coalesce(b.units,0) units, price*coalesce(units,0) pu from prices a
left join unitssold b
on a.product_id = b.product_id
and b.purchase_date between start_date and end_date ) l
group by 1

# Write your MySQL query statement below
select a.product_id, coalesce(round(sum(price*units)/sum(units),2),0) average_price  from prices a
left join unitssold b
on a.product_id = b.product_id
and b.purchase_date between start_date and end_date 
group by 1

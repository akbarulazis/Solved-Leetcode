# Write your MySQL query statement below
# 205ms
# select product_id, year first_year, quantity, price from (
#     select *,
#     row_number() over( partition by product_id order by year asc) row_num 
#     from sales ) k
#     where row_num = 1


select a.product_id, first_year, quantity, price from sales a
inner join ( select
product_id, min(year) first_year from sales
    group by 1
) b 
on a.product_id = b.product_id and year = first_year
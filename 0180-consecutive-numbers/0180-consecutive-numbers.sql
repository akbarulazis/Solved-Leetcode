# Write your MySQL query statement below


select distinct num ConsecutiveNums
 from (

select id, num, lead(num) over(order by id) num1,
    lag(num) over(order by id) num0
    from logs  ) k
    where num = num1 and num = num0 
    and num1 is not null and num0 is not null

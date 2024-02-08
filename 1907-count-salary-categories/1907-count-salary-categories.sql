# Write your MySQL query statement below

select a.category, coalesce(accounts_count,0) accounts_count from (
select 'Low Salary' Category
union 
select 'Average Salary' Category
union
select 'High Salary' Category)a
left join (

select case when income < 20000 then 'Low Salary'
    when income between 20000 and 50000 then 'Average Salary'
    else 'High Salary' end as category, count(*) accounts_count
    from accounts 
    group by 1
) b
    on a.category =b.category
  
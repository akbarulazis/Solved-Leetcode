# Write your MySQL query statement below
select class from (
select class, count(*) from courses 
    group by 1
having count(*) > 4 )k
     
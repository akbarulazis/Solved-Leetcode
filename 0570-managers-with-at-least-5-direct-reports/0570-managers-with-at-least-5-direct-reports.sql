# Write your MySQL query statement below
select name from employee e
inner join (
select managerid , count(*)
    from employee
    group by 1
    having count(*) > 4
) b
on e.id = b.managerid
# Write your MySQL query statement below

select distinct b.id from weather a
inner join weather b
on a.recordDate = b.recordDate - interval 1 day
where a.temperature < b.temperature
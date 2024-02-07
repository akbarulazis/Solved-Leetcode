# Write your MySQL query statement below

select person_name from queue a
inner join (
select turn, sum(weight) over (order by turn) total from queue
group by 1 ) b
on a.turn = b.turn
where total <= 1000
order by total desc
limit 1

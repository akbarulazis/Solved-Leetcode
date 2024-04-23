
select * from (
select name results from movieRating a
inner join users b
on a.user_id = b.user_id
group by b.user_id
order by count(*) desc , name asc
limit 1 ) k
union all
select * from (
select title results from movieRating a
inner join movies b
on a.movie_id = b.movie_id
where created_at between '2020-02-01' and '2020-02-29'
group by b.movie_id
order by avg(rating) desc , title asc
limit 1 ) e
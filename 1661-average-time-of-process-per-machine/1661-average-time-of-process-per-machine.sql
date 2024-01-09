# Write your MySQL query statement below
select a.machine_id, round(avg(b.timestamp-a.timestamp),3) processing_time from activity a
left join activity b
on a.machine_id = b.machine_id
and a.process_id = b.process_id
and b.activity_type = 'end'
where a.activity_type = 'start'
group by 1
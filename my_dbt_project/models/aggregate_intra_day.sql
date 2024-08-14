-- aggregate_intra_day.sql

with daily_aggregates as (
    select 
        date_trunc('day', timestamp::timestamp) as day,  -- Casting to timestamp
        avg(open) as avg_open,
        avg(high) as avg_high,
        avg(low) as avg_low,
        avg(close) as avg_close,
        sum(volume) as total_volume
    from {{ ref('transform_intra_day') }}
    group by day
)

select 
    day,
    avg_open,
    avg_high,
    avg_low,
    avg_close,
    total_volume
from daily_aggregates
order by day

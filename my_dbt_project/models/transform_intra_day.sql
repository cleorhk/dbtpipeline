-- transform_intra_day.sql

with raw_data as (
    select 
        timestamp, 
        "1. open" as open, 
        "2. high" as high, 
        "3. low" as low, 
        "4. close" as close, 
        "5. volume" as volume
    from public.intraday_data
)

select 
    timestamp,
    open,
    high,
    low,
    close,
    volume
from raw_data
where open is not null

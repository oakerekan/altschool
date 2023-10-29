"""
author: olayinkagaiusakerekan@gmail.com
"""
#latest1
question_one = """
select 
	txn_type, 
    count(txn_type) transaction_count
from 	
	raw.transactions
group by txn_type, ticker
having ticker = 'BTC'
"""

question_two = """
select 
	extract('Year' from txn_date::date) txn_year,
	txn_type,
	count(txn_time) txn_count,
	sum(quantity) total_quantity,
	avg(quantity) average_quantity
from raw.transactions
group by 1, 2, ticker
having ticker = 'BTC'
order by 1;
"""

question_three = """
with transaction_table as (
select 
        txn_type,
        ticker,
        extract(month from txn_date::date) calendar_num,
        to_char(to_date(txn_date, 'YYYY/MM/DD'), 'Mon') calendar_month,
        extract(Year from txn_date::date)  calendar_year
 from raw.transactions
 where ticker = 'ETH' and extract('Year' from txn_date::date) = 2020
)

select
    calendar_month,
    sum(case when txn_type = 'BUY' then 1 else 0 end) buy_quantity,
    sum(case when txn_type = 'SELL' then 1 else 0 end) sell_quantity
from transaction_table 
group by calendar_month, calendar_num
order by calendar_num;
"""

question_four = """
select 
	first_name, 
    sum(quantity) total_quantity
from 	
	raw.members m
inner join raw.transactions t
on m.member_id = t.member_id
group by 1, ticker
having ticker = 'BTC'
order by 2 desc 
limit 3
"""
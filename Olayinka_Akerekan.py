"""
author: olayinkagaiusakerekan@gmail.com
"""

question_one = """
select 
	txn_type, 
    count(txn_type) transaction_count
from 	
	raw.transactions
group by txn_type;
"""

question_two = """
select 
	extract('Year' from to_date(txn_date, 'YYYY/MM/DD')) txn_year,
	txn_type,
	count(txn_time) txn_count,
	sum(quantity) total_quantity,
	avg(quantity) average_quantity
from raw.transactions
group by 1, 2
order by 1;
"""
#midway
question_three = """
select
    calendar_month,
    sum(case when txn_type = 'BUY' then 1 else 0 end) buy_quantity,
    sum(case when txn_type = 'SELL' then 1 else 0 end) sell_quantity
from 
	(select 
        txn_type,
        ticker,
        to_char(to_date(txn_date, 'YYYY/MM/DD'), 'Mon') calendar_month,
        extract('Year' from to_date(txn_date, 'YYYY/MM/DD')) calendar_year
    from raw.transactions
    where ticker = 'ETH' and extract('Year' from to_date(txn_date, 'YYYY/MM/DD')) = 2020)
group by 1;
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
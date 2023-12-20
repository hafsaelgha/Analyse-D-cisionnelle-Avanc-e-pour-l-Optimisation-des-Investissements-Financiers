use Finance_warehouse;

create table fact_table  (
	pays_id int,
    country_name VARCHAR(255),
    category_name VARCHAR(255),
	date Date,
    Assets FLOAT,
    Liabilities FLOAT,
    Net_investment_position FLOAT,
    Revenue FLOAT,
    Expense FLOAT,
    Gross_operating_balance FLOAT,
	Total_investment FLOAT,
    GDP FLOAT,
    GDP_based_on_PPP FLOAT,
    Inflation FLOAT,
    Ease_of_doing_business FLOAT,
	unemployment_rate float
);
-------
insert into fact_table(pays_id, country_name, category_name, date)
select a.pays_id, a.country_name, c.category_name, a.date
from assets_dim a 
join country_dim c  
on a.pays_id = c.pays_id;
------
insert into fact_table(Assets)
select direct_investment + direct_investor_in_direct_investment_enterprises + equity_and_investment_fund_shares + financial_derivatives + other_investment + portfolio_investment + reserve_assets
from assets_dim;
------------
insert into fact_table(Liabilities)
select direct_investment + direct_investor_in_direct_investment_enterprises + equity_and_investment_fund_shares + financial_derivatives + other_investment + portfolio_investment
from liabilities_dim;
----------
insert into fact_table(Net_investment_position)
select Assets - Liabilities
from fact_table;
----------
insert into fact_table(Revenue, Expense, Gross_operating_balance)
select Revenue, Expense, Revenue-Expense
from operations_dim;
--------------
insert into fact_table(Total_investment, GDP, GDP_based_on_PPP)
select Total_investment, GDP, GDP_based_on_PPP
from national_accounts_dim;
----------------
insert into fact_table(inflation)
select valeur_infaltion
from inflation_dim;
--------------
insert into fact_table(Ease_of_doing_business)
select Ease_of_doing_business
from ease_of_doing_business_dim;
-----------
insert into fact_table(unemployment_rate)
select unemployement_rate
from unemployment_rate_dim;

select * from fact_table;


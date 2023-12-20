use Finance_warehouse;
create table country_dim  (
pays_id INT PRIMARY KEY,
country_name VARCHAR(255),
category_name VARCHAR(255),
capital VARCHAR(255),
longitude DECIMAL(10, 6),
latitude DECIMAL(10, 6),
currency VARCHAR(50),
continent VARCHAR(50)
);
BULK INSERT Finance_warehouse.dbo.country_dim
FROM 'C:\Users\Leno\Desktop\Data\country_info.csv'
WITH (
	FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2,   
	CODEPAGE = 'UTF-8'
);

select * from country_dim;
----------------
use Finance_warehouse;

create table assets_dim  (
pays_id INT FOREIGN KEY (pays_id) REFERENCES country_dim(pays_id),
country_name VARCHAR(255),
date DATE,
direct_investment float,
direct_investor_in_direct_investment_enterprises float,
equity_and_investment_fund_shares float,
financial_derivatives float,
other_investment float,
portfolio_investment float,
reserve_assets float
);

--loading--

BULK INSERT Finance_warehouse.dbo.assets_dim
FROM 'C:\Users\Leno\Desktop\Data\Assets\trasformed_Assets.csv'
WITH (
	FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2,
	DATAFILETYPE = 'char',
	CODEPAGE = 'ACP'
);
select * from assets_dim;
----------------
use Finance_warehouse;

create table liabilities_dim  (
pays_id int FOREIGN KEY (pays_id) REFERENCES country_dim(pays_id),
country_name VARCHAR(255),
date DATE,
direct_investment float,
direct_investor_in_direct_investment_enterprises float,
equity_and_investment_fund_shares float,
financial_derivatives float,
other_investment float,
portfolio_investment float
);

BULK INSERT Finance_warehouse.dbo.liabilities_dim
FROM 'C:\Users\Leno\Desktop\Data\Liabilities\trasformed_Liabilities.csv'
WITH (
	FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2,
	DATAFILETYPE = 'char',
	CODEPAGE = 'ACP'
);

select * from liabilities_dim;
--------------
use Finance_warehouse;

create table operations_dim  (
	pays_id int FOREIGN KEY (pays_id) REFERENCES country_dim(pays_id),
	country_name VARCHAR(255),
	date DATE,
	Revenue FLOAT,
	Taxes FLOAT,
    Social_contributions FLOAT,
    Other_revenue FLOAT,
    Expense FLOAT,
    Compensation_of_employees FLOAT,
    Use_of_goods_and_services FLOAT,
    Consumption_of_fixed_capital FLOAT,
    Interest FLOAT,
    Subsidies FLOAT,
    Social_benefits FLOAT,
    Other_expense FLOAT
);

BULK INSERT Finance_warehouse.dbo.operations_dim
FROM 'C:\Users\Leno\Desktop\Data\Operations\trasformed_Operations.csv'
WITH (
	FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2,
	DATAFILETYPE = 'char',
	CODEPAGE = 'ACP'
);

select * from operations_dim;
--------------
use Finance_warehouse;

create table import_export_dim  (
	pays_id int FOREIGN KEY (pays_id) REFERENCES country_dim(pays_id),
	country_name VARCHAR(255),
	date DATE,
	Volume_of_imports_of_goods_and_services FLOAT,
    Volume_of_exports_of_goods_and_services FLOAT
);

BULK INSERT Finance_warehouse.dbo.import_export_dim
FROM 'C:\Users\Leno\Desktop\Data\ImportExport\trasformed_Import_Export.csv'
WITH (
	FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2,
	DATAFILETYPE = 'char',
	CODEPAGE = 'ACP'
);
-------------------
use Finance_warehouse;

create table national_accounts_dim  (
	pays_id int FOREIGN KEY (pays_id) REFERENCES country_dim(pays_id),
	country_name VARCHAR(255),
	date DATE,
	GDP FLOAT,
    GDP_based_on_PPP FLOAT,
    Total_investment FLOAT
);

BULK INSERT Finance_warehouse.dbo.national_accounts_dim 
FROM 'C:\Users\Leno\Desktop\Data\National_Accounts\trasformed_National_Accounts.csv'
WITH (
	FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2,
	DATAFILETYPE = 'char',
	CODEPAGE = 'ACP'
);

select * from national_accounts_dim ;
--------------
use Finance_warehouse;

create table inflation_dim  (
	pays_id int FOREIGN KEY (pays_id) REFERENCES country_dim(pays_id),
	country_name VARCHAR(255),
	date DATE,
	valeur_infaltion float
);

BULK INSERT Finance_warehouse.dbo.inflation_dim
FROM 'C:\Users\Leno\Desktop\Data\Inflation\trasformed_Inflation.csv'
WITH (
	FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2,
	DATAFILETYPE = 'char',
	CODEPAGE = 'ACP'
);

select * from inflation_dim ;
---------------------------
use Finance_warehouse;

create table ease_of_doing_business_dim  (
	pays_id int FOREIGN KEY (pays_id) REFERENCES country_dim(pays_id),
	country_name VARCHAR(255),
	date DATE,
	ease_of_doing_business float
);

BULK INSERT Finance_warehouse.dbo.ease_of_doing_business_dim
FROM 'C:\Users\Leno\Desktop\Data\Ease of doing business\trasformed_Ease_of_doing_Bs.csv'
WITH (
	FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2,
	DATAFILETYPE = 'char',
	CODEPAGE = 'ACP'
);

select * from ease_of_doing_business_dim ;
-------------------


select * from import_export_dim;
----------------------
create table unemployment_rate(
	pays_id int not null,
    country_name VARCHAR(255),
	date date, 
	unemployement_rate float
);
select * from country_dim;
BULK INSERT Finance_warehouse.dbo.unemployment_rate
FROM 'C:\Users\Leno\Desktop\Data\Unemployment\trasformed_Unemployment.csv'
WITH (
	FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2,   
	CODEPAGE = 'UTF-8'
);

select * from unemployment_rate;





# Test for Data Engineering - ETL

Welcome to the Data Engineering ETL Test Project! This project provides a solution for a data engineering task by creating database schemas based on the Entity-Relationship Model (ER Model).

## Features

- Create database tables in MySQL.
- Upload CSV data to a database.
- Insert data in batch.
- Primary-Key validations in the CSV.

## Tech Stack

- Language: Python
- RDBMS: MySQL
- Version Control: Git (hosted on GitHub)


## Project Structure
```bash
.
├── app/                        # The main application directory.
│   ├── __init__.py             # Empty file to treat 'app' directory as a package.
│   ├── create_tables.py        # SQL scripts for Database table creation in MySQL.
│   ├── database_connector.py   # Created the connection with the database.
│   ├── extract_data.py         # DataExtraction class for data validation and extraction from the CSV data.
│   ├── load_data_into_db.py    # Data loading for a given table name.
├── data/                       # The data directory. It contains all the data files in .csv.
├── README.md                   # This file.
└── main.py                     # Entry point of.
```
## Notes
For the purpose of this test, data samples have been used due to limitations on data loading within Git. However, it's important to note that the ETL process implemented here is fully capable of handling and processing larger volumes of data. This demonstration with data samples showcases the functionality of the ETL system, which can be scaled to manage substantial datasets efficiently.


# Alamo Colleges ETL Data Pipeline

An end-to-end Python ETL (Extract, Transform, Load) pipeline designed to process, clean, and standardize student enrollment data. 

## Project Architecture
This pipeline demonstrates data engineering fundamentals using Python, Pandas, and SQLite, broken down into four modular scripts:

* **01_generate_data.py:** Generates a synthetic dataset mimicking raw, messy collegiate enrollment data (missing values, inconsistent formatting, duplicated records).
* **02_clean_data.py:** Utilizes Pandas to execute data standardization, handling null values, standardizing dates, and stripping whitespace.
* **03_load_data.py:** Establishes a connection to a local SQLite database (`alamo_enrollment.db`) and securely loads the transformed Pandas DataFrame into a relational table.
* **04_verify_data.py:** Executes SQL queries against the database to profile the data, verify row counts, and ensure data integrity post-load.

## Tech Stack
* **Language:** Python 3.x
* **Libraries:** Pandas, SQLite3, Datetime
* **Database:** SQLite
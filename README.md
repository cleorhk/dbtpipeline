# dbtpipeline
 This project is a comprehensive data pipeline designed to extract, transform, and load (ETL) data from various sources into a PostgreSQL database. It leverages dbt (data build tool) for managing SQL-based transformations and ensuring data quality, and integrates with other tools like Python for data extraction and Docker for containerization.

 Key Features
Data Extraction:

Utilizes Python to fetch intraday stock data from the Alpha Vantage API.
Stores raw data in CSV format for further processing.
Data Transformation:

Employs dbt to transform raw data into structured, analytics-ready tables.
Includes modular dbt models for efficient data processing.
Tests and documents data models to ensure data quality and clarity.
Data Loading:

Loads transformed data into a PostgreSQL database for easy access and querying.
Scalability and Automation:

Can be containerized with Docker for easy deployment and scalability.
Supports automated runs via task schedulers or orchestration tools.
Folder Structure
/my_dbt_project/: Contains all dbt-related files, including models and configurations.
/scripts/: Python scripts for data extraction and other ETL processes.
/data/: Stores raw and transformed data files.
/docker/: Docker configurations for containerizing the project.

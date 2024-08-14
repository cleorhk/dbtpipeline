import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

def export_to_postgres(input_file, db_url, table_name):
    # Load the transformed data from CSV
    df = pd.read_csv(input_file)

    # Create a database connection
    engine = create_engine(db_url)

    # Export the data to PostgreSQL
    df.to_sql(table_name, engine, if_exists='replace', index=False)
    print(f"Data exported to PostgreSQL table {table_name}")

if __name__ == "__main__":
    # Load environment variables from .env file
    load_dotenv()

    DB_USER = os.getenv('DB_USER')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    DB_HOST = os.getenv('DB_HOST')
    DB_PORT = os.getenv('DB_PORT')
    DB_NAME = os.getenv('DB_NAME')

    DB_URL = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    
    INPUT_FILE = 'transformed_data.csv'
    TABLE_NAME = 'intraday_data'
    
    export_to_postgres(INPUT_FILE, DB_URL, TABLE_NAME)

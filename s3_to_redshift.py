import os
import psycopg2
from dotenv import load_dotenv

def load_data_to_redshift(file_path, table_name):
    # Load environment variables from .env file
    load_dotenv()

    # Retrieve Redshift and S3 credentials from environment variables
    REDSHIFT_DB_NAME = os.getenv('REDSHIFT_DB_NAME')
    REDSHIFT_DB_USER = os.getenv('REDSHIFT_DB_USER')
    REDSHIFT_DB_PASSWORD = os.getenv('REDSHIFT_DB_PASSWORD')
    REDSHIFT_DB_PORT = os.getenv('REDSHIFT_DB_PORT')
    REDSHIFT_DB_HOST = os.getenv('REDSHIFT_DB_HOST')
    REDSHIFT_IAM_ROLE = os.getenv('REDSHIFT_IAM_ROLE')
    S3_BUCKET_NAME = os.getenv('S3_BUCKET_NAME')

    # Establish connection to Redshift
    conn = psycopg2.connect(
        dbname=REDSHIFT_DB_NAME,
        user=REDSHIFT_DB_USER,
        password=REDSHIFT_DB_PASSWORD,
        port=REDSHIFT_DB_PORT,
        host=REDSHIFT_DB_HOST
    )
    cur = conn.cursor()

    # Create table in Redshift
    create_table_query = f"""
    CREATE TABLE IF NOT EXISTS {table_name} (
        "timestamp" TIMESTAMP,
        "open" FLOAT,
        "high" FLOAT,
        "low" FLOAT,
        "close" FLOAT,
        "volume" INT
    );
    """
    cur.execute(create_table_query)
    conn.commit()

    # Copy data from S3 to Redshift
    copy_query = f"""
    COPY {table_name}
    FROM 's3://{S3_BUCKET_NAME}/{file_path}'
    IAM_ROLE '{REDSHIFT_IAM_ROLE}'
    CSV
    IGNOREHEADER 1
    TIMEFORMAT 'auto'
    EMPTYASNULL
    BLANKSASNULL
    DELIMITER ',';
    """
    cur.execute(copy_query)
    conn.commit()

    # Close the connection
    cur.close()
    conn.close()

if __name__ == "__main__":
    # Preprocess the CSV file
    os.system('python preprocess_csv.py')

    # Upload the cleaned CSV file to S3
    os.system('aws s3 cp transformed_data_clean.csv s3://your-bucket-name/transformed_data_clean.csv')

    FILE_PATH = 'transformed_data_clean.csv'  # The cleaned file path in the S3 bucket
    TABLE_NAME = 'intraday_data'  # The target table name in Redshift
    
    load_data_to_redshift(FILE_PATH, TABLE_NAME)

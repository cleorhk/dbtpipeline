import requests
import pandas as pd

def load_data(api_url, output_file):
    response = requests.get(api_url)
    data = response.json()

    # Extract the time series data
    time_series_key = 'Time Series (5min)'
    time_series_data = data.get(time_series_key, {})

    # Convert the time series data to a pandas DataFrame
    df = pd.DataFrame.from_dict(time_series_data, orient='index')
    df.index.name = 'timestamp'
    df.reset_index(inplace=True)

    # Save the DataFrame to a CSV file
    df.to_csv(output_file, index=False)
    print(f"Data loaded and saved to {output_file}")

if __name__ == "__main__":
    API_URL = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo'
    OUTPUT_FILE = 'raw_data.csv'
    load_data(API_URL, OUTPUT_FILE)

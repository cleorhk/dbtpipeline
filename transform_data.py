import pandas as pd

def transform_data(input_file, output_file):
    # Load the raw data from CSV
    df = pd.read_csv(input_file)

    # Transform the data: add a new column for the average price
    df['average_price'] = df[['1. open', '2. high', '3. low', '4. close']].mean(axis=1)

    # Save the transformed data to a new CSV file
    df.to_csv(output_file, index=False)
    print(f"Data transformed and saved to {output_file}")

if __name__ == "__main__":
    INPUT_FILE = 'raw_data.csv'
    OUTPUT_FILE = 'transformed_data.csv'
    transform_data(INPUT_FILE, OUTPUT_FILE)

import csv
import re

def preprocess_csv(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.DictReader(infile)
        
        # Map original headers to required headers
        header_map = {
            'timestamp': 'timestamp',
            '1. open': 'open',
            '2. high': 'high',
            '3. low': 'low',
            '4. close': 'close',
            '5. volume': 'volume'
        }
        
        # Define required fields
        required_fields = ['timestamp', 'open', 'high', 'low', 'close', 'volume']
        
        writer = csv.DictWriter(outfile, fieldnames=required_fields)
        writer.writeheader()
        
        for row in reader:
            # Map row to the new headers
            filtered_row = {new_key: row[old_key] for old_key, new_key in header_map.items()}
            writer.writerow(filtered_row)

if __name__ == "__main__":
    input_file = 'transformed_data.csv'
    output_file = 'transformed_data_clean.csv'
    preprocess_csv(input_file, output_file)

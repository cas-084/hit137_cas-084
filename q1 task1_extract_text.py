import pandas as pd

# List of CSV files to read
csv_files = ['CSV1.csv', 'CSV2.csv', 'CSV3.csv', 'CSV4.csv']

# Initialize an empty list to store text
all_text = []

# Loop through each CSV file
for file in csv_files:
    df = pd.read_csv(file)
    print(f"Processing {file}...")
    
    # Extract text from appropriate column
    if 'TEXT' in df.columns:
        all_text.extend(df['TEXT'].tolist())  # For CSV2, CSV3, CSV4
    elif 'SHORT-TEXT' in df.columns:
        all_text.extend(df['SHORT-TEXT'].tolist())  # For CSV1
    else:
        print(f"No valid text column found in {file}")

# Write all extracted text to a single .txt file
with open('consolidated_text.txt', 'w') as txt_file:
    for text in all_text:
        txt_file.write(text + "\n")  # Write each entry on a new line

print("Text from all CSV files has been extracted and saved to 'consolidated_text.txt'.")


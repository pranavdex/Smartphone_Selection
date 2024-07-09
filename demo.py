import pandas as pd

# Load the data
file_path = r'C:\Users\prana\Downloads\smartphones_cleaned_v7.csv'  # Use raw string to avoid unicode error
data = pd.read_csv(file_path)

# Sort the data alphabetically by brand and model
data_sorted = data.sort_values(by=['brand_name', 'model'])

# Save the sorted data to a new CSV file
data_sorted.to_csv(r'C:\Users\prana\Downloads\sorted_smartphones_by_brand.csv', index=False)  # Save file with raw string path

print("Data sorted and saved to 'sorted_smartphones_by_brand.csv'")




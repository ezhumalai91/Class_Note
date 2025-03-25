import pandas as pd

# Load the Excel file
file_path = 'names.xlsx'  # Replace with your file path
df = pd.read_excel(file_path, engine='openpyxl')  # Use 'xlrd' for older .xls files

# Display the DataFrame
print(df)

# Access specific columns
print("\nTamil Names:")
print(df['Tamil Name'])

print("\nEnglish Names:")
print(df['English Name'])

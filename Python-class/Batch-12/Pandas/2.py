import pandas as pd

# Function to calculate grade based on average
def calculate_grade(average):
    if average >= 90:
        return 'A+'
    elif average >= 80:
        return 'A'
    elif average >= 70:
        return 'B+'
    elif average >= 60:
        return 'B'
    elif average >= 50:
        return 'C+'
    elif average >= 40:
        return 'C'
    else:
        return 'F'

# Load the Excel file
file_path = 'student_marks.xlsx'  # Replace with your file path
df = pd.read_excel(file_path)
print(df)

# Initialize columns for calculations
df['Total Marks'] = df.iloc[:, 2:].sum(axis=1)  # Sum across subject columns
print(df['Total Marks'])
print(df.shape[1])
df['Average'] = df['Total Marks'] / (df.shape[1] - 2)  # Average calculation
print(df['Average'])
df['Grade'] = df['Average'].apply(calculate_grade)  # Apply grade calculation

# # Define pass/fail criteria (e.g., 40% average to pass)
df['Result'] = df['Average'].apply(lambda avg: 'Pass' if avg >= 40 else 'Fail')
print(df['Result'])
# # Display the DataFrame with calculations
# print(df)

# # Save the result to a new Excel file
output_file_path = 'student_marks_with_results.xlsx'
df.to_excel(output_file_path, index=False)

# print(f"Results saved to {output_file_path}")

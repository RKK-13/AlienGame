import pandas as pd

# Load your Excel file using openpyxl engine.
df = pd.read_excel(r'C:\Users\Ranji\python\Learnings\trypandaex.xlsx', engine='openpyxl')

# Strip any extra spaces from column names
df.columns = df.columns.str.strip()

# Fill forward the 'Jobs' column to propagate job titles down
df['Jobs'] = df['Jobs'].ffill()

# Group by 'Jobs' and aggregate the 'Description' column
merged_df = df.groupby('Jobs', as_index=False)['Description'].agg(' '.join)

# Save the cleaned data back to an Excel file using openpyxl engine.
merged_df.to_excel(r'C:\Users\Ranji\python\Learnings\alterclean_file.xlsx', index=False, engine='openpyxl')


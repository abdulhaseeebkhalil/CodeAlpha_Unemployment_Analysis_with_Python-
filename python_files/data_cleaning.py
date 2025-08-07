import pandas as pd

# Load the datasets
df_india = pd.read_csv("D:/Internships/CodeAlpha/Project/CodeAlpha_Unemployment_Analysis_with_Python-/Main_files/data/UnemploymentinIndia.csv")
df_rate = pd.read_csv( "D:/Internships/CodeAlpha/Project/CodeAlpha_Unemployment_Analysis_with_Python-/Main_files/data/Unemployment_Rate_upto_11_2020.csv")

# Clean column names by stripping leading/trailing spaces
def clean_col_names(df):
    cols = df.columns
    new_cols = []
    for col in cols:
        new_cols.append(col.strip())
    df.columns = new_cols
    return df

df_india = clean_col_names(df_india)
df_rate = clean_col_names(df_rate)

# Drop rows with missing values in df_india
df_india.dropna(inplace=True)

# Convert 'Date' column to datetime objects
df_india['Date'] = pd.to_datetime(df_india['Date'], dayfirst=True)
df_rate['Date'] = pd.to_datetime(df_rate['Date'], dayfirst=True)

# Convert 'Estimated Employed' to int in df_india
df_india['Estimated Employed'] = df_india['Estimated Employed'].astype(int)

# Display info and head after cleaning
print("\nUnemployment in India (df_india) info after cleaning:")
df_india.info()
print("\nUnemployment Rate upto 11_2020 (df_rate) info after cleaning:")
df_rate.info()

print("\nUnemployment in India (df_india) head after cleaning:")
print(df_india.head())
print("\nUnemployment Rate upto 11_2020 (df_rate) head after cleaning:")
print(df_rate.head())

# Save cleaned data (optional, but good practice)
df_india.to_csv("D:/Internships/CodeAlpha/Project/CodeAlpha_Unemployment_Analysis_with_Python-/Main_files/data/UnemploymentinIndia_cleaned.csv", index=False)
df_rate.to_csv("D:/Internships/CodeAlpha/Project/CodeAlpha_Unemployment_Analysis_with_Python-/Main_files/data/Unemployment_Rate_upto_11_2020_cleaned.csv", index=False)



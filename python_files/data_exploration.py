import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the datasets
df_india = pd.read_csv('D:/Internships/CodeAlpha/Project/CodeAlpha_Unemployment_Analysis_with_Python-/Main_files/data/UnemploymentinIndia.csv')
df_rate = pd.read_csv('D:/Internships/CodeAlpha/Project/CodeAlpha_Unemployment_Analysis_with_Python-/Main_files/data/Unemployment_Rate_upto_11_2020.csv')

print('Unemployment in India (df_india) info:')
print(df_india.info())
print('\nUnemployment Rate upto 11_2020 (df_rate) info:')
print(df_rate.info())

print('\nUnemployment in India (df_india) head:')
print(df_india.head())
print('\nUnemployment Rate upto 11_2020 (df_rate) head:')
print(df_rate.head())

print('\nUnemployment in India (df_india) shape:', df_india.shape)
print('Unemployment Rate upto 11_2020 (df_rate) shape:', df_rate.shape)

print('\nUnemployment in India (df_india) columns:')
print(df_india.columns.tolist())
print('\nUnemployment Rate upto 11_2020 (df_rate) columns:')
print(df_rate.columns.tolist())

print('\nUnemployment in India (df_india) missing values:')
print(df_india.isnull().sum())
print('\nUnemployment Rate upto 11_2020 (df_rate) missing values:')
print(df_rate.isnull().sum())

print('\nUnemployment in India (df_india) data types:')
print(df_india.dtypes)
print('\nUnemployment Rate upto 11_2020 (df_rate) data types:')
print(df_rate.dtypes)


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load the cleaned datasets
df_india = pd.read_csv("D:/Internships/CodeAlpha/Project/CodeAlpha_Unemployment_Analysis_with_Python-/Main_files/data/UnemploymentinIndia_cleaned.csv")
df_rate = pd.read_csv("D:/Internships/CodeAlpha/Project/CodeAlpha_Unemployment_Analysis_with_Python-/Main_files/data/Unemployment_Rate_upto_11_2020_cleaned.csv")

# Convert 'Date' column to datetime objects
df_india["Date"] = pd.to_datetime(df_india["Date"])
df_rate["Date"] = pd.to_datetime(df_rate["Date"])

# Filter data for the Covid-19 period (e.g., March 2020 onwards)
covid_start_date = pd.to_datetime("2020-03-01")
df_rate_covid = df_rate[df_rate["Date"] >= covid_start_date]
df_india_covid = df_india[df_india["Date"] >= covid_start_date]

# Overall Unemployment Rate during Covid-19
fig_covid_unemployment = px.line(df_rate_covid, x='Date', y='Estimated Unemployment Rate (%)', title='Unemployment Rate During Covid-19 Period (March 2020 onwards)')
fig_covid_unemployment.write_image("D:/Internships/CodeAlpha/Project/CodeAlpha_Unemployment_Analysis_with_Python-/Main_files/visuals/covid_unemployment_rate.png")

# Regional impact of Covid-19 on unemployment
fig_regional_covid_impact = px.line(df_rate_covid, x='Date', y='Estimated Unemployment Rate (%)', color='Region', title='Regional Impact of Covid-19 on Unemployment')
fig_regional_covid_impact.write_image("D:/Internships/CodeAlpha/Project/CodeAlpha_Unemployment_Analysis_with_Python-/Main_files/visuals/regional_covid_impact.png")

# Rural vs Urban impact during Covid-19
fig_area_covid_impact = px.line(df_india_covid, x='Date', y='Estimated Unemployment Rate (%)', color='Area', title='Rural vs Urban Unemployment During Covid-19')
fig_area_covid_impact.write_image("D:/Internships/CodeAlpha/Project/CodeAlpha_Unemployment_Analysis_with_Python-/Main_files/visuals/area_covid_impact.png")

# Seasonality (re-emphasize with monthly average)
df_india["Month_name"] = df_india["Date"].dt.strftime("%b")
monthly_avg_unemployment = df_india.groupby('Month_name')['Estimated Unemployment Rate (%)'].mean().reset_index()

# Order months correctly
month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
monthly_avg_unemployment['Month_name'] = pd.Categorical(monthly_avg_unemployment['Month_name'], categories=month_order, ordered=True)
monthly_avg_unemployment = monthly_avg_unemployment.sort_values('Month_name')

plt.figure(figsize=(10, 6))
plt.plot(monthly_avg_unemployment['Month_name'], monthly_avg_unemployment['Estimated Unemployment Rate (%)'], marker='o')
plt.title('Seasonal Trends in Unemployment Rate (Monthly Average)')
plt.xlabel('Month')
plt.ylabel('Average Unemployment Rate (%)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("D:/Internships/CodeAlpha/Project/CodeAlpha_Unemployment_Analysis_with_Python-/Main_files/visuals/seasonal_unemployment_trends.png")

# Before and after Covid-19 comparison
pre_covid = df_rate[df_rate["Date"] < covid_start_date]
post_covid = df_rate[df_rate["Date"] >= covid_start_date]

pre_covid_avg = pre_covid['Estimated Unemployment Rate (%)'].mean()
post_covid_avg = post_covid['Estimated Unemployment Rate (%)'].mean()

print(f"Average unemployment rate before Covid-19: {pre_covid_avg:.2f}%")
print(f"Average unemployment rate during Covid-19: {post_covid_avg:.2f}%")
print(f"Increase in unemployment rate due to Covid-19: {post_covid_avg - pre_covid_avg:.2f}%")

# Highest unemployment rates during Covid-19
highest_unemployment = df_rate_covid.nlargest(10, 'Estimated Unemployment Rate (%)')
print("\nTop 10 highest unemployment rates during Covid-19:")
print(highest_unemployment[['Region', 'Date', 'Estimated Unemployment Rate (%)']].to_string(index=False))

print("\nCovid-19 impact analysis and pattern identification completed.")


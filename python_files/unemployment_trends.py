import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load the cleaned datasets
df_india = pd.read_csv("D:/Internships/CodeAlpha/Project/CodeAlpha_Unemployment_Analysis_with_Python-/Main_files/data/UnemploymentinIndia_cleaned.csv")
df_rate = pd.read_csv("D:/Internships/CodeAlpha/Project/CodeAlpha_Unemployment_Analysis_with_Python-/Main_files/data/Unemployment_Rate_upto_11_2020_cleaned.csv")

# Convert 'Date' column to datetime objects (again, as it's loaded from CSV)
df_india["Date"] = pd.to_datetime(df_india["Date"])
df_rate["Date"] = pd.to_datetime(df_rate["Date"])

# Overall Unemployment Rate over time (df_rate)
fig_overall_unemployment = px.line(df_rate, x='Date', y='Estimated Unemployment Rate (%)', title='Overall Estimated Unemployment Rate Over Time')
fig_overall_unemployment.write_image("D:/Internships/CodeAlpha/Project/CodeAlpha_Unemployment_Analysis_with_Python-/Main_files/visuals/overall_unemployment_rate.png")

# Unemployment Rate by Region (df_rate)
fig_region_unemployment = px.bar(df_rate, x='Region', y='Estimated Unemployment Rate (%)', color='Region', title='Estimated Unemployment Rate by Region', animation_frame='Date', animation_group='Region')
fig_region_unemployment.write_image("D:/Internships/CodeAlpha/Project/CodeAlpha_Unemployment_Analysis_with_Python-/Main_files/visuals/region_unemployment_rate.png")

# Unemployment Rate by Area (Rural/Urban) (df_india)
fig_area_unemployment = px.bar(df_india, x='Area', y='Estimated Unemployment Rate (%)', color='Area', title='Estimated Unemployment Rate by Area (Rural/Urban)', animation_frame='Date', animation_group='Area')
fig_area_unemployment.write_image("D:/Internships/CodeAlpha/Project/CodeAlpha_Unemployment_Analysis_with_Python-/Main_files/visuals/area_unemployment_rate.png")

# Heatmap of Unemployment Rate by Region and Month (df_india)
df_india['Month'] = df_india['Date'].dt.month
df_india["Month_int"] = df_india["Month"].apply(lambda x: int(x))
df_india["Month_name"] = df_india["Date"].dt.strftime("%b")

month_map = {
    1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr", 5: "May", 6: "Jun",
    7: "Jul", 8: "Aug", 9: "Sep", 10: "Oct", 11: "Nov", 12: "Dec"
}
df_india["Month_name"] = df_india["Month_int"].map(month_map)


plt.figure(figsize=(12, 8))
sns.heatmap(df_india.pivot_table(values='Estimated Unemployment Rate (%)', index='Region', columns='Month_name'), annot=True, cmap='YlGnBu', fmt='.1f')
plt.title('Unemployment Rate Heatmap by Region and Month')
plt.tight_layout()
plt.savefig("D:/Internships/CodeAlpha/Project/CodeAlpha_Unemployment_Analysis_with_Python-/Main_files/visuals/unemployment_heatmap_region_month.png")

print("Visualizations generated and saved to D:/Internships/CodeAlpha/Project/CodeAlpha_Unemployment_Analysis_with_Python-/Main_files/visuals/")



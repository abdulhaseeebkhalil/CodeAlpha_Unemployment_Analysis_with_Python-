import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.set_page_config(layout="wide")
st.title("📊 Unemployment Analysis in India")

@st.cache_data
def load_and_clean_data():
    df_india = pd.read_csv("data/UnemploymentinIndia.csv")
    df_rate = pd.read_csv("data/Unemployment_Rate_upto_11_2020.csv")

    # Clean column names
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
    df_india["Date"] = pd.to_datetime(df_india["Date"], dayfirst=True)
    df_rate["Date"] = pd.to_datetime(df_rate["Date"], dayfirst=True)

    # Convert 'Estimated Employed' to int in df_india
    df_india["Estimated Employed"] = df_india["Estimated Employed"].astype(int)

    return df_india, df_rate

df_india, df_rate = load_and_clean_data()

st.header("1. Data Overview and Cleaning")
st.write("Initial data exploration and cleaning steps have been performed. Missing values were handled, column names cleaned, and data types converted.")

st.subheader("Unemployment in India (df_india) - First 5 rows")
st.dataframe(df_india.head())

st.subheader("Unemployment Rate upto 11_2020 (df_rate) - First 5 rows")
st.dataframe(df_rate.head())

st.header("2. Unemployment Trends Analysis")

# Overall Unemployment Rate over time (df_rate)
st.subheader("Overall Estimated Unemployment Rate Over Time")
fig_overall_unemployment = px.line(df_rate, x='Date', y='Estimated Unemployment Rate (%)', title='Overall Estimated Unemployment Rate Over Time')
st.plotly_chart(fig_overall_unemployment, use_container_width=True)

# Unemployment Rate by Region (df_rate)
st.subheader("Estimated Unemployment Rate by Region")
fig_region_unemployment = px.bar(df_rate, x='Region', y='Estimated Unemployment Rate (%)', color='Region', title='Estimated Unemployment Rate by Region', animation_frame='Date', animation_group='Region')
st.plotly_chart(fig_region_unemployment, use_container_width=True)

# Unemployment Rate by Area (Rural/Urban) (df_india)
st.subheader("Estimated Unemployment Rate by Area (Rural/Urban)")
fig_area_unemployment = px.bar(df_india, x='Area', y='Estimated Unemployment Rate (%)', color='Area', title='Estimated Unemployment Rate by Area (Rural/Urban)', animation_frame='Date', animation_group='Area')
st.plotly_chart(fig_area_unemployment, use_container_width=True)

# Heatmap of Unemployment Rate by Region and Month (df_india)
st.subheader("Unemployment Rate Heatmap by Region and Month")
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
st.pyplot(plt)

st.header("3. Covid-19 Impact Analysis")

covid_start_date = pd.to_datetime("2020-03-01")
df_rate_covid = df_rate[df_rate["Date"] >= covid_start_date]
df_india_covid = df_india[df_india["Date"] >= covid_start_date]

# Overall Unemployment Rate during Covid-19
st.subheader("Unemployment Rate During Covid-19 Period (March 2020 onwards)")
fig_covid_unemployment = px.line(df_rate_covid, x='Date', y='Estimated Unemployment Rate (%)', title='Unemployment Rate During Covid-19 Period (March 2020 onwards)')
st.plotly_chart(fig_covid_unemployment, use_container_width=True)

# Regional impact of Covid-19 on unemployment
st.subheader("Regional Impact of Covid-19 on Unemployment")
fig_regional_covid_impact = px.line(df_rate_covid, x='Date', y='Estimated Unemployment Rate (%)', color='Region', title='Regional Impact of Covid-19 on Unemployment')
st.plotly_chart(fig_regional_covid_impact, use_container_width=True)

# Rural vs Urban impact during Covid-19
st.subheader("Rural vs Urban Unemployment During Covid-19")
fig_area_covid_impact = px.line(df_india_covid, x='Date', y='Estimated Unemployment Rate (%)', color='Area', title='Rural vs Urban Unemployment During Covid-19')
st.plotly_chart(fig_area_covid_impact, use_container_width=True)

# Seasonality (re-emphasize with monthly average)
st.subheader("Seasonal Trends in Unemployment Rate (Monthly Average)")
df_india["Month_name"] = df_india["Date"].dt.strftime("%b")
monthly_avg_unemployment = df_india.groupby('Month_name')['Estimated Unemployment Rate (%)'].mean().reset_index()

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
st.pyplot(plt)

# Before and after Covid-19 comparison
pre_covid = df_rate[df_rate["Date"] < covid_start_date]
post_covid = df_rate[df_rate["Date"] >= covid_start_date]

pre_covid_avg = pre_covid['Estimated Unemployment Rate (%)'].mean()
post_covid_avg = post_covid['Estimated Unemployment Rate (%)'].mean()

st.subheader("Unemployment Rate Before and During Covid-19")
st.write(f"Average unemployment rate before Covid-19: {pre_covid_avg:.2f}%")
st.write(f"Average unemployment rate during Covid-19: {post_covid_avg:.2f}%")
st.write(f"Increase in unemployment rate due to Covid-19: {post_covid_avg - pre_covid_avg:.2f}%")

# Highest unemployment rates during Covid-19
highest_unemployment = df_rate_covid.nlargest(10, 'Estimated Unemployment Rate (%)')
st.subheader("Top 10 Highest Unemployment Rates During Covid-19")
st.dataframe(highest_unemployment[['Region', 'Date', 'Estimated Unemployment Rate (%)']])

st.header("4. Key Insights and Conclusions")
st.write("""
### Key Findings:
- The Covid-19 pandemic significantly impacted unemployment rates in India, with an average increase of 3.73%.
- Puducherry experienced the highest unemployment rate during the pandemic at 75.85% in April 2020.
- Rural and urban areas were both affected, but with different patterns of recovery.
- Seasonal trends show variations in unemployment throughout the year.
- Regional disparities exist, with some states being more vulnerable to economic shocks.

### Policy Implications:
- Targeted interventions needed for severely affected regions like Puducherry, Jharkhand, and Bihar.
- Seasonal preparedness programs can help mitigate predictable unemployment spikes.
- Robust economic policies and social safety nets are essential for future crisis preparedness.
""")


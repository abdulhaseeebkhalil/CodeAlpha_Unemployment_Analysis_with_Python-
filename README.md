## 📊 Unemployment Analysis with Python

This project focuses on analyzing unemployment trends in a given dataset, using Python for **data cleaning**, **exploration**, and **visualization**. It also investigates the impact of the **Covid‑19 pandemic** on unemployment rates and uncovers key patterns or seasonal trends to inform potential economic and social policies.

---

### 📁 Project Structure

```
Unemployment_Analysis_with_Python/
│
├── data/
│   └── unemployment.csv         # Dataset (raw or cleaned)
│
├── notebooks/
│   └── analysis.ipynb          # Main Jupyter Notebook with full analysis
│
├── visuals/
│   └── unemployment_trends.png # Saved graphs & plots
│
├── README.md                   # Project summary and instructions
└── requirements.txt            # List of required libraries
```

---

### 🧪 Objectives

* Analyze **unemployment rate data** representing the percentage of unemployed individuals.
* Perform **data cleaning** to handle missing values, incorrect types, and formatting issues.
* Explore **unemployment trends** using descriptive statistics and visual analytics.
* Identify how **Covid-19 impacted** employment patterns over time.
* Detect **key patterns**, such as **seasonality**, **gender** or **region-based trends**.
* Generate insights that may support **policy-making** and **economic decision-making**.

---

### 📌 Tools & Technologies

* **Python** (Pandas, NumPy, Matplotlib, Seaborn, Plotly)
* **Jupyter Notebook**
* **Data Visualization**
* (Optional) **Time series decomposition / forecasting models**

---

### ✅ Expected Output

* Cleaned dataset
* Visual trends and heatmaps
* Timeline of unemployment spikes (esp. during Covid-19)
* Summary of insights and suggestions

---

### 💡 Analysis and Insights

#### Data Overview and Cleaning

Two datasets were used for this analysis:

1.  `UnemploymentinIndia.csv`: Contains detailed unemployment data across various regions and areas (rural/urban).
2.  `Unemployment_Rate_upto_11_2020.csv`: Provides unemployment rates up to November 2020, including geographical coordinates.

Initial data exploration revealed that `UnemploymentinIndia.csv` had 28 rows with missing values, which were subsequently dropped. Column names in both datasets were cleaned by stripping leading/trailing spaces. The 'Date' columns were converted to datetime objects, and 'Estimated Employed' in `df_india` was converted to integer type for consistency and accurate calculations.

#### Unemployment Trends and Visualizations

Several visualizations were generated to understand unemployment trends:

*   **Overall Estimated Unemployment Rate Over Time**: A line plot showing the general trend of unemployment rates. This visualization highlights fluctuations and overall patterns in unemployment.

*   **Estimated Unemployment Rate by Region**: A bar chart visualizing unemployment rates across different regions. This helps in identifying regions with consistently high or low unemployment.

*   **Estimated Unemployment Rate by Area (Rural/Urban)**: A bar chart comparing unemployment rates between rural and urban areas, providing insights into regional disparities.

*   **Unemployment Rate Heatmap by Region and Month**: A heatmap illustrating the unemployment rate across different regions and months. This helps in identifying seasonal patterns and regional variations throughout the year.

#### Covid-19 Impact Analysis

The analysis specifically focused on the period from March 2020 onwards to assess the impact of the Covid-19 pandemic on unemployment rates. Key findings include:

*   **Average Unemployment Rate Comparison**: The average unemployment rate before Covid-19 (prior to March 2020) was **9.23%**. During the Covid-19 period (March 2020 onwards), the average unemployment rate rose to **12.96%**, indicating a significant increase of **3.73%**.

*   **Overall Unemployment Rate During Covid-19**: A line plot showing the unemployment rate specifically during the pandemic period, highlighting the sharp increase and subsequent fluctuations.

*   **Regional Impact of Covid-19**: A line plot illustrating how different regions were affected by the pandemic in terms of unemployment, revealing varying degrees of impact across states.

*   **Rural vs Urban Unemployment During Covid-19**: A line plot comparing rural and urban unemployment rates during the pandemic, showing how both areas were affected.

*   **Top 10 Highest Unemployment Rates During Covid-19**: The analysis identified specific instances of extremely high unemployment during the pandemic. For example:
    *   Puducherry: 75.85% (April 2020)
    *   Jharkhand: 59.23% (May 2020)
    *   Puducherry: 58.19% (May 2020)
    *   Tamil Nadu: 49.83% (April 2020)
    *   Jharkhand: 47.09% (April 2020)
    *   Bihar: 46.64% (April 2020)
    *   Bihar: 45.96% (May 2020)
    *   Haryana: 43.22% (April 2020)
    *   Delhi: 42.27% (May 2020)
    *   Tripura: 41.23% (April 2020)

#### Seasonal Trends

Analysis of monthly average unemployment rates revealed seasonal patterns, which are crucial for understanding recurring trends independent of major events like the pandemic. The `Seasonal Trends in Unemployment Rate (Monthly Average)` plot provides a clear visual of these patterns.

### 📈 Visualizations

All generated visualizations are saved in the `visuals/` directory:

*   `overall_unemployment_rate.png`
*   `region_unemployment_rate.png`
*   `area_unemployment_rate.png`
*   `unemployment_heatmap_region_month.png`
*   `covid_unemployment_rate.png`
*   `regional_covid_impact.png`
*   `area_covid_impact.png`
*   `seasonal_unemployment_trends.png`

---

### 🚀 Conclusion and Policy Implications

This analysis provides a clear picture of unemployment trends in India, particularly highlighting the significant impact of the Covid-19 pandemic. The insights gained can inform policy-making by:

*   **Targeted Interventions**: Identifying regions and areas most affected by unemployment (e.g., Puducherry, Jharkhand, Bihar during Covid-19) allows for targeted economic relief and job creation programs.
*   **Seasonal Preparedness**: Understanding seasonal trends can help in preparing for periods of higher unemployment and implementing proactive measures.
*   **Disaster Preparedness**: The sharp increase during Covid-19 underscores the need for robust economic policies and social safety nets to mitigate the impact of future crises.

Further analysis could involve time series forecasting to predict future unemployment rates and more in-depth investigation into specific regional economic factors.

---

**Author**: Abdul Haseeb
**Date**: 8/7/2025



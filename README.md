##  Indonesia Village Fund Analysis - Analyzing Budget vs. Realization

This is a Python script for analyzing the budget (pagu) vs. realization (realisasi) of village funds in Indonesia. It utilizes pandas for data manipulation and seaborn for visualizations.

**Functionality:**

1. **Data Loading:** Reads data from CSV files containing pagu and realisasi information (assuming they reside in a folder named "data").
2. **Data Cleaning:** Merges the dataframes based on common columns and drops rows with missing values.
3. **Feature Engineering:** Calculates the utilization rate (realisasi divided by pagu).
4. **Visualization:**
    * Creates a scatter plot to visualize the relationship between pagu and utilization.
    * Generates a normal distribution plot to analyze the distribution of the utilization rate.

**How to Use:**

1. Ensure you have pandas and seaborn libraries installed (`pip install pandas seaborn`).
2. Place your pagu and realisasi data in a folder named "data" within the same directory as this script.
3. Run the script (`python village_fund_analysis.py`).

**Expected Output:**

* Two visualizations will be displayed:
    * A scatter plot showing pagu on the x-axis and utilization rate on the y-axis.
    * A normal distribution plot of the utilization rate.

**Further Enhancements:**

* Implement additional data cleaning techniques (e.g., handling outliers).
* Explore other visualizations like box plots or heatmaps for deeper insights.
* Integrate machine learning models for more advanced analysis (e.g., predicting future utilization).

**Disclaimer:**

This script provides a basic framework for analyzing village fund data. It may require adjustments based on the specific data format and desired analysis goals.

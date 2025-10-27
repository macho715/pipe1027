import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from io import StringIO

# Step 1: Load the data from the provided text (simulating the CSV content)
# In a real environment, replace with pd.read_csv('almk_constraints_report.csv')
data_text = """aisle,occupied_sqm,cap_sqm,utilization,over_cap
A1,534.5,396.0,134.97,True
A2,534.93,396.0,135.08,True
A3,526.42,396.0,132.93,True
A4,509.95,396.0,128.78,True
A5,530.98,396.0,134.09,True
A6,520.31,396.0,131.39,True
A7,0.0,396.0,0.0,False
A8,0.0,396.0,0.0,False"""

df = pd.read_csv(StringIO(data_text))

# Step 2: Filter for utilized aisles (occupied_sqm > 0) to focus on relevant data
df = df[df["occupied_sqm"] > 0]

# Step 3: Sort the data by occupied_sqm in descending order to prioritize high-occupancy aisles
df_sorted = df.sort_values(by="occupied_sqm", ascending=False).reset_index(drop=True)

# Step 4: Calculate the total occupied sqm across all aisles
total_occupied = df_sorted["occupied_sqm"].sum()

# Step 5: Calculate the cumulative sum of occupied sqm
df_sorted["cumulative_occupied"] = df_sorted["occupied_sqm"].cumsum()

# Step 6: Calculate the cumulative percentage of total occupied space
df_sorted["cumulative_percentage"] = (df_sorted["cumulative_occupied"] / total_occupied) * 100

# Step 7: Identify the Pareto point (aisles contributing to 80% of occupied sqm)
pareto_threshold = 80
pareto_aisles = df_sorted[df_sorted["cumulative_percentage"] <= pareto_threshold]["aisle"].tolist()
print(f"Aisles contributing to {pareto_threshold}% of occupied sqm: {pareto_aisles}")

# Step 8: Plot the Pareto chart for visual analysis
fig, ax1 = plt.subplots(figsize=(10, 6))

# Bar plot for individual occupied sqm per aisle
ax1.bar(df_sorted["aisle"], df_sorted["occupied_sqm"], color="b")
ax1.set_xlabel("Aisle")
ax1.set_ylabel("Occupied SQM", color="b")
ax1.tick_params(axis="y", labelcolor="b")

# Line plot for cumulative percentage
ax2 = ax1.twinx()
ax2.plot(df_sorted["aisle"], df_sorted["cumulative_percentage"], color="r", marker="o")
ax2.set_ylabel("Cumulative Percentage (%)", color="r")
ax2.tick_params(axis="y", labelcolor="r")

# Add horizontal line at 80% threshold for Pareto reference
ax2.axhline(y=pareto_threshold, color="g", linestyle="--", label=f"{pareto_threshold}% Threshold")

plt.title("Pareto Analysis of Warehouse Aisle Occupancy")
plt.legend()
plt.show()

# Step 9: Generate recommendations based on Pareto analysis
top_aisles_count = len(pareto_aisles)
print(
    f"Recommendation: Prioritize space optimization in the top {top_aisles_count} aisles, which account for {pareto_threshold}% of total occupied space."
)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from io import StringIO

# Step 1: Load the data from the provided text (simulating the CSV content)
# In a real environment, replace with pd.read_csv('almk_constraints_report.csv')
data_text = """aisle,occupied_sqm,cap_sqm,utilization,over_cap
A1,534.5,396.0,134.97,True
A2,534.93,396.0,135.08,True
A3,526.42,396.0,132.93,True
A4,509.95,396.0,128.78,True
A5,530.98,396.0,134.09,True
A6,520.31,396.0,131.39,True
A7,0.0,396.0,0.0,False
A8,0.0,396.0,0.0,False"""

df = pd.read_csv(StringIO(data_text))

# Step 2: Filter for utilized aisles (occupied_sqm > 0) to focus on relevant data
df = df[df['occupied_sqm'] > 0]

# Step 3: Sort the data by occupied_sqm in descending order to prioritize high-occupancy aisles
df_sorted = df.sort_values(by='occupied_sqm', ascending=False).reset_index(drop=True)

# Step 4: Calculate the total occupied sqm across all aisles
total_occupied = df_sorted['occupied_sqm'].sum()

# Step 5: Calculate the cumulative sum of occupied sqm
df_sorted['cumulative_occupied'] = df_sorted['occupied_sqm'].cumsum()

# Step 6: Calculate the cumulative percentage of total occupied space
df_sorted['cumulative_percentage'] = (df_sorted['cumulative_occupied'] / total_occupied) * 100

# Step 7: Identify the Pareto point (aisles contributing to 80% of occupied sqm)
pareto_threshold = 80
pareto_aisles = df_sorted[df_sorted['cumulative_percentage'] <= pareto_threshold]['aisle'].tolist()
print(f"Aisles contributing to {pareto_threshold}% of occupied sqm: {pareto_aisles}")

# Step 8: Plot the Pareto chart for visual analysis
fig, ax1 = plt.subplots(figsize=(10, 6))

# Bar plot for individual occupied sqm per aisle
ax1.bar(df_sorted['aisle'], df_sorted['occupied_sqm'], color='b')
ax1.set_xlabel('Aisle')
ax1.set_ylabel('Occupied SQM', color='b')
ax1.tick_params(axis='y', labelcolor='b')

# Line plot for cumulative percentage
ax2 = ax1.twinx()
ax2.plot(df_sorted['aisle'], df_sorted['cumulative_percentage'], color='r', marker='o')
ax2.set_ylabel('Cumulative Percentage (%)', color='r')
ax2.tick_params(axis='y', labelcolor='r')

# Add horizontal line at 80% threshold for Pareto reference
ax2.axhline(y=pareto_threshold, color='g', linestyle='--', label=f'{pareto_threshold}% Threshold')

plt.title('Pareto Analysis of Warehouse Aisle Occupancy')
plt.legend()
plt.show()

# Step 9: Generate recommendations based on Pareto analysis
top_aisles_count = len(pareto_aisles)
print(f"Recommendation: Prioritize space optimization in the top {top_aisles_count} aisles, which account for {pareto_threshold}% of total occupied space.")

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("indian_road_accidents_demo.csv")

# Display first few rows
print("Sample Data:")
print(df.head())

# Basic info
print("\nDataset Info:")
print(df.info())

print("\nSummary Statistics:")
print(df.describe())

# Total accidents by year
accidents_by_year = df.groupby("Year")["Total_Accidents"].sum()
print("\nTotal Accidents by Year:")
print(accidents_by_year)

plt.figure(figsize=(8,5))
accidents_by_year.plot(kind="bar")
plt.title("Total Road Accidents in India (2018–2022)")
plt.xlabel("Year")
plt.ylabel("Total Accidents")
plt.tight_layout()
plt.show()

# Top 5 states by total accidents
top_states = df.groupby("State/UT")["Total_Accidents"].sum().sort_values(ascending=False).head(5)
print("\nTop 5 States by Total Accidents:")
print(top_states)

plt.figure(figsize=(8,5))
top_states.plot(kind="bar")
plt.title("Top 5 States by Total Accidents")
plt.xlabel("State/UT")
plt.ylabel("Total Accidents")
plt.tight_layout()
plt.show()

# Fatality rate analysis
df["Fatality_Rate"] = (df["Fatal_Accidents"] / df["Total_Accidents"]) * 100

fatality_by_year = df.groupby("Year")["Fatality_Rate"].mean()
print("\nAverage Fatality Rate by Year (%):")
print(fatality_by_year)

plt.figure(figsize=(8,5))
fatality_by_year.plot(marker="o")
plt.title("Average Fatality Rate Over Years")
plt.xlabel("Year")
plt.ylabel("Fatality Rate (%)")
plt.grid(True)
plt.tight_layout()
plt.show()

# Correlation analysis
correlation = df[["Total_Accidents", "Fatal_Accidents", "Deaths", "Injuries"]].corr()
print("\nCorrelation Matrix:")
print(correlation)

plt.figure(figsize=(6,5))
plt.imshow(correlation, cmap="coolwarm", interpolation="nearest")
plt.xticks(range(len(correlation)), correlation.columns, rotation=45)
plt.yticks(range(len(correlation)), correlation.columns)
plt.colorbar()
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()

# NumPy example: Accident growth rate year to year
years = np.array(sorted(df["Year"].unique()))
totals = np.array([df[df["Year"]==y]["Total_Accidents"].sum() for y in years])
growth_rates = np.diff(totals) / totals[:-1] * 100

print("\nYearly Growth Rates (%):")
for i, g in enumerate(growth_rates):
    print(f"{years[i]} → {years[i+1]}: {g:.2f}%")

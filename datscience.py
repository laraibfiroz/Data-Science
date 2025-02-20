import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Load the dataset
file_path = r"C:\Users\larai\OneDrive\Desktop\Data Science\archive\Road Accident Data.csv"
df = pd.read_csv(file_path)

# Display basic information about the dataset
print("Dataset Overview:")
print(df.info())
print("\nBasic Statistics:")
print(df.describe())

# Frequency of Accidents Over Time
df['Accident Date'] = pd.to_datetime(df['Accident Date'])  # Ensure 'Accident Date' column is in datetime format
df['Year'] = df['Accident Date'].dt.year
df['Month'] = df['Accident Date'].dt.month
df['DayOfWeek'] = df['Accident Date'].dt.dayofweek

def plot_countplot(column, title, xlabel):
    plt.figure(figsize=(12,6))
    sns.countplot(x=column, data=df, palette='Blues')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel("Number of Accidents")
    plt.xticks(rotation=45)
    plt.show()

plot_countplot('Year', "Accident Frequency Over the Years", "Year")
plot_countplot('Month', "Accidents by Month", "Month")
plot_countplot('DayOfWeek', "Accidents by Day of the Week", "Day of the Week")

# Geographical Distribution of Accidents
plt.figure(figsize=(12,6))
sns.scatterplot(x=df['Longitude'], y=df['Latitude'], alpha=0.5)
plt.title("Geographical Distribution of Accidents")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.show()

# Severity Analysis
plot_countplot('Accident_Severity', "Distribution of Accident Severities", "Severity")

# Environmental and Road Conditions
plot_countplot('Weather_Conditions', "Weather Conditions During Accidents", "Weather Conditions")
plot_countplot('Road_Type', "Accidents by Road Type", "Road Type")
plot_countplot('Light_Conditions', "Accidents by Lighting Conditions", "Lighting Conditions")

# Vehicle and Driver Information
plot_countplot('Vehicle_Type', "Vehicle Types Involved in Accidents", "Vehicle Type")

# Temporal Patterns
plot_countplot('DayOfWeek', "Accidents by Day of the Week", "Day of the Week")

# Contributing Factors
plot_countplot('Carriageway_Hazards', "Contributing Factors to Accidents", "Factors")

# Injury and Fatality Analysis
plot_countplot('Number_of_Casualties', "Distribution of Casualties in Accidents", "Number of Casualties")

# Comparative Analysis
plot_countplot('Urban_or_Rural_Area', "Accident Distribution by Urban or Rural Areas", "Area Type")

# Save the processed dataset for further use
df.to_csv("processed_road_accidents.csv", index=False)

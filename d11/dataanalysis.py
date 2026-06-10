import pandas as pd
import numpy as np

df = pd.read_csv("employees.csv")

# Remove duplicates
df = df.drop_duplicates()

# Handle missing values
df["Age"] = df["Age"].fillna(df["Age"].mean())

# Median
df["Salary"] = df["Salary"].fillna(df["Salary"].median())

# Mode
df["Department"] = df["Department"].fillna(df["Department"].mode()[0])

# Remove invalid ages
print(df[df["Age"] > 100])

df = df[(df["Age"] > 0) & (df["Age"] <= 100)]

# Check missing values
print(df.isnull().sum())

# Basic analysis
print("Average Salary:", df["Salary"].mean())
print("Maximum Salary:", df["Salary"].max())
print(df["Department"].value_counts())

print(df.head())

# handling nulls
print(df.isnull())

# df = df.dropna()

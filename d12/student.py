import pandas as pd
df = pd.read_csv("student_data.csv")
df["Age_Group"] = pd.cut(df["Age"],bins =[0,25,40,100],labels = ["Young","Adult","Senior"])
print(df.isnull().sum())
df_backup = df.copy()
df["Study_Hours"] = df["Study_Hours"].fillna(df["Study_Hours"].mean().round())
df = df.dropna(subset=["Marks"])
df = df_backup.copy()
print(df.shape)
corr_matrix = df.corr(numeric_only=True)

print(corr_matrix)
print(df)

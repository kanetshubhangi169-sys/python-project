import pandas as pd

df = pd.read_csv("trainee.csv")
print(df)

df["Age_Group"] = pd.cut(df["Age"],bins =[0,25,40,100],labels = ["Young","Adult","Senior"])


df["Salary_Category"] = pd.cut(df["Salary"],bins = [0,50000,70000,100000],labels = ["Low","medium","high"])

df["Experience_Level"] = pd.cut(df["Experience"],bins=[0, 2, 5, 10],labels=["Beginner", "Intermediate", "Expert"])

df["Is_IT"] = (df["Department"] == "IT").astype(int)

df["Username"] = (df["Email"].str.split("@").str[0])

df["Joining_Date"] = pd.to_datetime(df["Joining_Date"])

df["Joining_Year"] = (df["Joining_Date"].dt.year)
df["Joining_Month"] = (df["Joining_Date"].dt.month)
df["Joining_Day"] = (df["Joining_Date"].dt.day_name())

current_year = 2026
df["Years_At_Company"] = (current_year - df["Joining_Date"].dt.year)

df["Double_Salary"] = (df["Salary"] * 2)

print(df)
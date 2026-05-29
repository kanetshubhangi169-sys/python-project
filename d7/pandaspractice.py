#series
import pandas as pd

data = [10,20,30,40]

s = pd.Series(data)
print(s)

#custom index
s = pd.Series([10,20,30], index=["a","b","c"])

print(s)

#access a series value
print(s["a"])


#dataframe
import pandas as pd

data = {"Name": ["A", "B", "C"],"Marks": [80, 90, 70]}

df = pd.DataFrame(data)

print(df)

#access a column
import pandas as pd
data = {"Name": ["A", "B", "C"],"Marks": [80, 90, 70]}

df = pd.DataFrame(data)

print(df["Name"])

#access a row
import pandas as pd
data = {"Name": ["A", "B", "C"],"Marks": [80, 90, 70]}

df = pd.DataFrame(data)
print(df.loc[0])

print(df.iloc[1])


#lambda function 
import pandas as pd

data = {"Marks": [80,90,70]}

df = pd.DataFrame(data)

df["Marks"] = df["Marks"].apply(lambda x:x ** 1)

print(df)
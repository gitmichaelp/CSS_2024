# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 09:48:16 2024

@author: pmichael
"""

import pandas as pd

file =pd.read_excel("C:/Users/pmichael/css_Day2/data_02/residentdoctors.xlsx")

file = pd.read_json("C:/Users/pmichael/css_Day2/data_02/student_data.json")


df =pd.read_excel("C:/Users/pmichael/css_Day2/data_02/residentdoctors.xlsx")
print(df.info())

#extracting certain values from strings

df["LOWER_AGE"] = df["AGEDIST"].str.extract('(\d+)-')


df["UPPER_AGE"] = df["AGEDIST"].str.extract('-(\d+)')


print(df.info())

#convert to interger
df["LOWER_AGE"] = df["LOWER_AGE"].astype(int)

print(df.info())

df = pd.read_csv("C:/Users/pmichael/css_Day2/data_02/time_series_data.csv", index_col=0)

print(df.info())

df["Date"] = pd.to_datetime(df["Date"], format= "%Y-%m-%d")

print(df.info())

#splitting the date into year, month and day

df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month
df["Day"] = df["Date"].dt.day



df = pd.read_csv('data_02/patient_data_dates.csv', index_col=0)

# Allows you to see all rows
pd.set_option('display.max_rows',None)


df.drop(index=26, inplace = True)

df["Date"] = pd.to_datetime(df["Date"])

#df['Date'] = df['Date'].str.strip()

avg_cal = df["Calories"].mean()

#filling nans with an average value

df["Calories"].fillna(avg_cal, inplace=True)

#drop nan & naTBvalues

df.dropna(inplace=True)

#Replacing values in a column

df["Duration"] = df["Duration"].replace([450], 50)

print((df))

df =pd.read_csv("C:/Users/pmichael/css_Day2/data_02/iris.csv")

col_names = df.columns

print(col_names)


df["sepal_length_sq"] =df['sepal_length']**2

grouped = df.groupby("class")


#mean square value

MSV = grouped["sepal_length_sq"].mean()

print(MSV)

#striping a variable in a column

df["class"] = df["class"].str.replace("Iris-", "")

#choosing variables in a mixed variable class

df_larger_than5 = df[df['sepal_length']>5]

print(df[df["class"]=="virginica"])





























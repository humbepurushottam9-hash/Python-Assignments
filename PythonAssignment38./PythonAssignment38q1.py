import pandas as pd

df = pd.read_csv("student_performance_ml(1).csv")

print("First 5 Records:")
print(df.head())

print("\nLast 5 Records:")
print(df.tail())

print("\nTotal number of Rows and Columns:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nData Types of Each Column:")
print(df.dtypes)
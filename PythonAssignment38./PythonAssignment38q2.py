import pandas as pd

df = pd.read_csv("student_performance_ml(1).csv")

print("Total number of Students: ",len(df))

passed = (df["FinalResult"] == 1).sum()
print("Number of Students passed: ",passed)

failed = (df["FinalResult"] == 0).sum()
print("Number of students failed: ",failed)
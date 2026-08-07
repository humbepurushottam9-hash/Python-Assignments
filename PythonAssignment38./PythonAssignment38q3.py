import pandas as pd

df = pd.read_csv("student_performance_ml(1).csv")

print("Average Study Hours: ",df["StudyHours"].mean())

print("Average Attendence: ",df["Attendance"].mean())

print("Maximum Previous score: ",df["PreviousScore"].max())

print("Minimum Sleep Hours: ",df["SleepHours"].min())
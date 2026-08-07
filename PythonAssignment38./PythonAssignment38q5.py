import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("student_performance_ml(1).csv")

plt.hist(df["StudyHours"], bins = 10, edgecolor = "black")

plt.title("Histogram of Study Hours")
plt.xlabel("Study Hours")
plt.ylabel("Number of students")

plt.show()
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("student_performance_ml(1).csv")

plt.boxplot(df["Attendance"])

plt.title("Boxplot of Attendance")
plt.ylabel("Attendance (%)")

plt.show()
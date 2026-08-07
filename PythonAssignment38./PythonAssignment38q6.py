import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("student_performance_ml(1).csv")

plt.scatter(df["StudyHours"], df["PreviousScore"])

plt.title("Study Hours vs Previous Score")
plt.xlabel("Study Hours")
plt.ylabel("Previous Score")

plt.show()
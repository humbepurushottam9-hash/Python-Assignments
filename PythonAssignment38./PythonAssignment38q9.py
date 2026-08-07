import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("student_performance_ml(1).csv")

df.boxplot(column = "SleepHours", by = "FinalResult")

plt.title("Sleep Hours vs Fianl Result")
plt.suptitle("")
plt.xlabel("Final Result(0 = Fail, 1 = Pass)")
plt.ylabel("Sleep Hours")

plt.show()
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("student_performance_ml(1).csv")

df.boxplot(column = "AssignmentsCompleted", by = "FinalResult")

plt.title("Assignments Completed vs Final Result")
plt.suptitle("")
plt.xlabel("Fianl Result = ( 0 = Fail, 1 = Pass)")
plt.ylabel("Assignments Completed")

plt.show()
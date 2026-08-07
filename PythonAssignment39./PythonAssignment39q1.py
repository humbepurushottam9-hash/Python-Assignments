import pandas as pd
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv("student_performance_ml(1).csv")

X = df[["StudyHours", "Attendance", "PreviousScore",
        "AssignmentsCompleted", "SleepHours"]]

y = df["FinalResult"]

model = DecisionTreeClassifier(random_state=42)

model.fit(X, y)

print("Decision Tree model trained successfully.")
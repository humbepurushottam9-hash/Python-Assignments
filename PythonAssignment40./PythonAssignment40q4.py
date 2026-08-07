import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# Load the dataset
df = pd.read_csv("student_performance_ml(1).csv")

X = df[["StudyHours",
        "Attendance",
        "PreviousScore",
        "AssignmentsCompleted",
        "SleepHours"]]

y = df["FinalResult"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42
)

model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

new_students = pd.DataFrame({
    "StudyHours": [6, 2, 8, 4, 7],
    "Attendance": [85, 60, 95, 70, 88],
    "PreviousScore": [66, 45, 90, 55, 78],
    "AssignmentsCompleted": [7, 3, 10, 5, 8],
    "SleepHours": [7, 5, 8, 6, 7]
})

predictions = model.predict(new_students)

print("Predicted Results:")
print(predictions)
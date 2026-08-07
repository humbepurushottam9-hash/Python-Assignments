import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

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

y_pred = model.predict(X_test)

misclassified = X_test[y_test != y_pred]

print("Misclassified Students:")
print(misclassified)

print("\nActual Values:")
print(y_test[y_test != y_pred].values)

print("\nPredicted Values:")
print(y_pred[y_test != y_pred])

count = (y_test != y_pred).sum()
print("\nNumber of Misclassified Students:", count)
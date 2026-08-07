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
    X, y, test_size=0.2, random_state=42
)


model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

print("Feature Importance Scores:\n")

for feature, importance in zip(X.columns, model.feature_importances_):
    print(f"{feature} : {importance:.4f}")

most_important = X.columns[model.feature_importances_.argmax()]
least_important = X.columns[model.feature_importances_.argmin()]

print("\nMost Important Feature :", most_important)
print("Least Important Feature:", least_important)
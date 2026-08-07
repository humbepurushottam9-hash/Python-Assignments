import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load the dataset
df = pd.read_csv("student_performance_ml(1).csv")

####################################################
# Create a new feature
####################################################

df["PerformanceIndex"] = (df["StudyHours"] * 2) + df["Attendance"]

####################################################
# Train model with original features
####################################################

X1 = df[["StudyHours",
         "Attendance",
         "PreviousScore",
         "AssignmentsCompleted",
         "SleepHours"]]

y = df["FinalResult"]

X_train, X_test, y_train, y_test = train_test_split(
    X1, y, test_size=0.20, random_state=42
)

model1 = DecisionTreeClassifier(random_state=42)
model1.fit(X_train, y_train)

y_pred1 = model1.predict(X_test)

accuracy1 = accuracy_score(y_test, y_pred1)

####################################################
# Train model with new PerformanceIndex feature
####################################################

X2 = df[["StudyHours",
         "Attendance",
         "PreviousScore",
         "AssignmentsCompleted",
         "SleepHours",
         "PerformanceIndex"]]

X_train, X_test, y_train, y_test = train_test_split(
    X2, y, test_size=0.20, random_state=42
)

model2 = DecisionTreeClassifier(random_state=42)
model2.fit(X_train, y_train)

y_pred2 = model2.predict(X_test)

accuracy2 = accuracy_score(y_test, y_pred2)

####################################################
# Compare Accuracies
####################################################

print("Accuracy without PerformanceIndex : {:.2f}%".format(accuracy1 * 100))
print("Accuracy with PerformanceIndex    : {:.2f}%".format(accuracy2 * 100))
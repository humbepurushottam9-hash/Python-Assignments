import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load the dataset
df = pd.read_csv("student_performance_ml(1).csv")

####################################################
# Model with all features
####################################################

X = df[["StudyHours",
        "Attendance",
        "PreviousScore",
        "AssignmentsCompleted",
        "SleepHours"]]

y = df["FinalResult"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42
)

model1 = DecisionTreeClassifier(random_state=42)
model1.fit(X_train, y_train)

y_pred1 = model1.predict(X_test)

accuracy1 = accuracy_score(y_test, y_pred1)

####################################################
# Model after removing SleepHours
####################################################

X_new = df[["StudyHours",
            "Attendance",
            "PreviousScore",
            "AssignmentsCompleted"]]

X_train, X_test, y_train, y_test = train_test_split(
    X_new, y, test_size=0.20, random_state=42
)

model2 = DecisionTreeClassifier(random_state=42)
model2.fit(X_train, y_train)

y_pred2 = model2.predict(X_test)

accuracy2 = accuracy_score(y_test, y_pred2)

####################################################
# Compare Accuracy
####################################################

print("Accuracy with SleepHours      : {:.2f}%".format(accuracy1 * 100))
print("Accuracy without SleepHours   : {:.2f}%".format(accuracy2 * 100))
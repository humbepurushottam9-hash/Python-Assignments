import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

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

####################################################
# Manual Accuracy Calculation
####################################################

correct_predictions = (y_test == y_pred).sum()

total_predictions = len(y_test)

manual_accuracy = (correct_predictions / total_predictions) * 100

####################################################
# Accuracy using sklearn
####################################################

sklearn_accuracy = accuracy_score(y_test, y_pred) * 100

####################################################
# Display Results
####################################################

print("Correct Predictions :", correct_predictions)
print("Total Predictions   :", total_predictions)

print("\nManual Accuracy  : {:.2f}%".format(manual_accuracy))
print("Sklearn Accuracy : {:.2f}%".format(sklearn_accuracy))

if round(manual_accuracy, 2) == round(sklearn_accuracy, 2):
    print("\nResult: Both accuracies match.")
else:
    print("\nResult: Accuracies do not match.")
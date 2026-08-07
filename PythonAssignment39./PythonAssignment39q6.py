import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv("student_performance_ml(1).csv")

X = df[["StudyHours", "Attendance", "PreviousScore",
        "AssignmentsCompleted", "SleepHours"]]
y = df["FinalResult"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model1 = DecisionTreeClassifier(max_depth=1, random_state=42)
model1.fit(X_train, y_train)
y_pred1 = model1.predict(X_test)
acc1 = accuracy_score(y_test, y_pred1)

model2 = DecisionTreeClassifier(max_depth=3, random_state=42)
model2.fit(X_train, y_train)
y_pred2 = model2.predict(X_test)
acc2 = accuracy_score(y_test, y_pred2)

model3 = DecisionTreeClassifier(max_depth=None, random_state=42)
model3.fit(X_train, y_train)
y_pred3 = model3.predict(X_test)
acc3 = accuracy_score(y_test, y_pred3)

print("Testing Accuracy with max_depth = 1    : {:.2f}%".format(acc1 * 100))
print("Testing Accuracy with max_depth = 3    : {:.2f}%".format(acc2 * 100))
print("Testing Accuracy with max_depth = None : {:.2f}%".format(acc3 * 100))
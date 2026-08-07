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

model1 = DecisionTreeClassifier(random_state=0)
model1.fit(X_train, y_train)
y_pred1 = model1.predict(X_test)
acc1 = accuracy_score(y_test, y_pred1)

model2 = DecisionTreeClassifier(random_state=10)
model2.fit(X_train, y_train)
y_pred2 = model2.predict(X_test)
acc2 = accuracy_score(y_test, y_pred2)

model3 = DecisionTreeClassifier(random_state=43)
model3.fit(X_train, y_train)
y_pred3 = model3.predict(X_test)
acc3 = accuracy_score(y_test, y_pred3)

print("Testing Accuracy (random_state = 0)  : {:.2f}%".format(acc1 * 100))
print("Testing Accuracy (random_state = 10) : {:.2f}%".format(acc2 * 100))
print("Testing Accuracy (random_state = 43) : {:.2f}%".format(acc3 * 100))
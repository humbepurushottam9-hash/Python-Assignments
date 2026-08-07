import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load the dataset
df = pd.read_csv("student_performance_ml(1).csv")

####################################################
# Model using all features
####################################################

X_full = df[["StudyHours",
             "Attendance",
             "PreviousScore",
             "AssignmentsCompleted",
             "SleepHours"]]

y = df["FinalResult"]

X_train, X_test, y_train, y_test = train_test_split(
    X_full, y, test_size=0.20, random_state=42
)

model_full = DecisionTreeClassifier(random_state=42)
model_full.fit(X_train, y_train)

y_pred_full = model_full.predict(X_test)

full_accuracy = accuracy_score(y_test, y_pred_full)

####################################################
# Model using only StudyHours and Attendance
####################################################

X_small = df[["StudyHours", "Attendance"]]

X_train, X_test, y_train, y_test = train_test_split(
    X_small, y, test_size=0.20, random_state=42
)

model_small = DecisionTreeClassifier(random_state=42)
model_small.fit(X_train, y_train)

y_pred_small = model_small.predict(X_test)

small_accuracy = accuracy_score(y_test, y_pred_small)

####################################################
# Compare Accuracy
####################################################

print("Accuracy using all features      : {:.2f}%".format(full_accuracy * 100))
print("Accuracy using 2 features only   : {:.2f}%".format(small_accuracy * 100))
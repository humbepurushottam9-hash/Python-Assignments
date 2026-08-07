###############################################################
# Machine Learning Practical
# Student Performance Prediction using Decision Tree
#
# This program performs:
# 1. Dataset Handling
# 2. Data Analysis
# 3. Data Visualization
# 4. Train-Test Split
# 5. Model Training
# 6. Prediction
# 7. Accuracy Calculation
# 8. Confusion Matrix Generation
# 9. Final Conclusion
###############################################################

# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay

###############################################################
# STEP 1 : DATASET HANDLING
###############################################################

print("\n========== DATASET HANDLING ==========\n")

# Load dataset
df = pd.read_csv("student_performance_ml(1).csv")

# Display first 5 records
print("First 5 Records")
print(df.head())

# Display last 5 records
print("\nLast 5 Records")
print(df.tail())

# Display shape
print("\nRows and Columns :", df.shape)

# Display column names
print("\nColumn Names")
print(df.columns.tolist())

# Display datatypes
print("\nData Types")
print(df.dtypes)

###############################################################
# STEP 2 : DATA ANALYSIS
###############################################################

print("\n========== DATA ANALYSIS ==========\n")

print("Total Students :", len(df))

print("\nPass/Fail Count")
print(df["FinalResult"].value_counts())

print("\nPass/Fail Percentage")
print(df["FinalResult"].value_counts(normalize=True) * 100)

print("\nAverage Study Hours :", df["StudyHours"].mean())
print("Average Attendance :", df["Attendance"].mean())
print("Maximum Previous Score :", df["PreviousScore"].max())
print("Minimum Sleep Hours :", df["SleepHours"].min())

###############################################################
# STEP 3 : DATA VISUALIZATION
###############################################################

print("\n========== DATA VISUALIZATION ==========\n")

# Histogram
plt.figure(figsize=(6,4))
plt.hist(df["StudyHours"], bins=10, edgecolor="black")
plt.title("Histogram of Study Hours")
plt.xlabel("Study Hours")
plt.ylabel("Frequency")
plt.show()

# Scatter Plot
plt.figure(figsize=(6,4))
plt.scatter(df["StudyHours"], df["PreviousScore"])
plt.title("Study Hours vs Previous Score")
plt.xlabel("Study Hours")
plt.ylabel("Previous Score")
plt.show()

# Boxplot
plt.figure(figsize=(5,4))
plt.boxplot(df["Attendance"])
plt.title("Attendance Boxplot")
plt.ylabel("Attendance")
plt.show()

###############################################################
# STEP 4 : TRAIN TEST SPLIT
###############################################################

print("\n========== TRAIN TEST SPLIT ==========\n")

# Input Features
X = df[[
    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted",
    "SleepHours"
]]

# Target Variable
y = df["FinalResult"]

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

print("Training Samples :", len(X_train))
print("Testing Samples :", len(X_test))

###############################################################
# STEP 5 : MODEL TRAINING
###############################################################

print("\n========== MODEL TRAINING ==========\n")

model = DecisionTreeClassifier(random_state=42)

model.fit(X_train, y_train)

print("Decision Tree Model Trained Successfully")

###############################################################
# STEP 6 : PREDICTION
###############################################################

print("\n========== MODEL PREDICTION ==========\n")

# Predict test data
y_pred = model.predict(X_test)

print("Predicted Values")
print(y_pred)

print("\nActual Values")
print(y_test.values)

# Predict new student
new_student = [[6, 85, 66, 7, 7]]

prediction = model.predict(new_student)

print("\nPrediction for New Student")

if prediction[0] == 1:
    print("Student will PASS")
else:
    print("Student will FAIL")

###############################################################
# STEP 7 : ACCURACY CALCULATION
###############################################################

print("\n========== ACCURACY ==========\n")

# Training Accuracy
train_pred = model.predict(X_train)
train_accuracy = accuracy_score(y_train, train_pred)

# Testing Accuracy
test_accuracy = accuracy_score(y_test, y_pred)

print("Training Accuracy : {:.2f}%".format(train_accuracy * 100))
print("Testing Accuracy  : {:.2f}%".format(test_accuracy * 100))

###############################################################
# STEP 8 : CONFUSION MATRIX
###############################################################

print("\n========== CONFUSION MATRIX ==========\n")

cm = confusion_matrix(y_test, y_pred)

print(cm)

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=["Fail", "Pass"]
)

disp.plot(cmap="Blues")
plt.title("Confusion Matrix")
plt.show()

###############################################################
# STEP 9 : FINAL CONCLUSION
###############################################################

print("\n========== FINAL CONCLUSION ==========\n")

print("1. Dataset loaded successfully.")
print("2. Data analyzed using Pandas.")
print("3. Visualizations created using Matplotlib.")
print("4. Dataset split into Training and Testing sets.")
print("5. Decision Tree model trained successfully.")
print("6. Predictions generated successfully.")
print("7. Training and Testing accuracy calculated.")
print("8. Confusion Matrix generated.")
print("9. The model predicts whether a student will PASS or FAIL based on:")
print("   - Study Hours")
print("   - Attendance")
print("   - Previous Score")
print("   - Assignments Completed")
print("   - Sleep Hours")
print("\nMachine Learning Practical Completed Successfully.")
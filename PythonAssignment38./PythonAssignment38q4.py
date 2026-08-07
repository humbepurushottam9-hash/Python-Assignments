import pandas as pd

df = pd.read_csv("student_performance_ml(1).csv")

result_count = df["FinalResult"].value_counts()

print("Distribbution of FinalResult:")
print(result_count)

percentage = (df["FinalResult"].value_counts(normalize = True) * 100)

print("\nPercentage of Pass and fail Students: ")
print(percentage)
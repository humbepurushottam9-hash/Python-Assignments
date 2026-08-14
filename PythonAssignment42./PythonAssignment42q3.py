import math


def calculate_distance(study_hours1, attendance1, study_hours2, attendance2):
    distance = math.sqrt(
        (study_hours1 - study_hours2) ** 2 +
        (attendance1 - attendance2) ** 2
    )

    return distance


def main():

    # Dataset
    dataset = [
        (2, 60, "Fail"),
        (5, 80, "Pass"),
        (6, 85, "Pass"),
        (1, 50, "Fail")
    ]

    # Accept input from user
    study_hours = float(input("Enter Study Hours: "))
    attendance = float(input("Enter Attendence: "))

    # Calculate distances
    distances = []

    for hours, attend, result in dataset:

        distance = calculate_distance(
            study_hours,
            attendance,
            hours,
            attend
        )

        distances.append((distance, result))

    # Sort distances
    distances.sort()

    # K = 3
    k = 3

    # Select 3 nearest neighbors
    nearest_neighbors = distances[:k]

    # Majority voting
    pass_count = 0
    fail_count = 0

    for distance, result in nearest_neighbors:

        if result == "Pass":
            pass_count += 1
        else:
            fail_count += 1

    # Predict result
    if pass_count > fail_count:
        predicted_result = "Pass"
    else:
        predicted_result = "Fail"

    print("\nPredicted Result :", predicted_result)


if __name__ == "__main__":
    main()
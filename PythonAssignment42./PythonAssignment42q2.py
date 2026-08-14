import math

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def predict_class(dataset, x, y, k):

    distances = []

    # Calculate distance from new point to every dataset point
    for point, px, py, label in dataset:

        distance = calculate_distance(x, y, px, py)

        distances.append((distance, point, label))

    # Sort distances
    distances.sort()

    # Select K nearest neighbors
    nearest_neighbors = distances[:k]

    # Majority voting
    red_count = 0
    blue_count = 0

    for distance, point, label in nearest_neighbors:

        if label =="Red":
            red_count += 1
        else:
            blue_count += 1

    # Predict class
    if red_count > blue_count:
        return "Red"
    else:
        return "Blue"

def main():

    # Dataset
    dataset = [
        ("A",1,2,"Red"),
        ("B",2,3,"Red"),
        ("C",3,1,"Blue"),
        ("D",6,5,"Blue"),
    ]

    # new data point
    x = float(input("Enter X coordinate: "))
    y = float(input("Enter Y coordinates: "))

    print("Predicted Results")

    # Test different values of k
    for k in [1, 2, 3, 4]:

        result = predict_class(dataset, x, y, k)

        print(f"K = {k} -> {result}")

if __name__=="__main__":
    main()
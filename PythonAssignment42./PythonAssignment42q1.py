import math

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def main():

    # Dataset
    dataset = [
        ("A",1,2,"Red"),
        ("B",2,3,"Red"),
        ("C",3,1,"Blue"),
        ("D",6,5,"Blue"),
    ]

    # accept new point
    x = float(input("Enter X coordinate: "))
    y = float(input("Enter Y coordinate: "))

    # Calculate distances
    distances = []

    for point, px, py, label in dataset:

        distance = calculate_distance(x, y, px, py)

        distances.append((distance, point, label))

    # Sort distances
    distances.sort()

    # Select K = 3 nearest neighbors
    k = 3
    nearest_neighbors = distances[:k]

    print("Nearest Neighbors: ")

    # Display nearest neighbors
    for distance, point, label in nearest_neighbors:
        print(f"{point} - Distance: {distance:.2f}")

    # Majority voting
    red_count = 0
    blue_count = 0

    for distance, point, label in nearest_neighbors:

        if label == "Red":
            red_count += 1
        else:
            blue_count += 1

    # Predict class
    if red_count > blue_count:
        predicted_class = "Red"
    else:
        predicted_class = "Blue"

    print("Predicted class is: ",predicted_class)

if __name__=="__main__":
    main()
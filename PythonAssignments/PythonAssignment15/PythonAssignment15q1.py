def main():
    Data = list(map(int, input("Enter numbers separated by space: ").split()))

    Squares = list(map(lambda No: No * No, Data))

    print("Original List :", Data)
    print("Squares List  :", Squares)

if __name__ == "__main__":
    main()
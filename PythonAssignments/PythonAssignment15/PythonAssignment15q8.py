def main():
    Data = list(map(int, input("Enter numbers separated by space: ").split()))

    Result = list(filter(lambda No: No % 3 == 0 and No % 5 == 0, Data))

    print("Original List :", Data)
    print("Numbers divisible by 3 and 5 :", Result)

if __name__ == "__main__":
    main()
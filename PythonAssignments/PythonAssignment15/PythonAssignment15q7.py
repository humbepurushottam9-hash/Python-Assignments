def main():
    Data = input("Enter strings separated by space: ").split()

    Result = list(filter(lambda Str: len(Str) < 5, Data))

    print("Original List :", Data)
    print("Strings with length less than 5 :", Result)

if __name__ == "__main__":
    main()
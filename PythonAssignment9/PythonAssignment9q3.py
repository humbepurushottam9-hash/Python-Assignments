def Square(No):
    No = No * No
    print("Square of given number is:\n",No)

def main():
    Value = int(input("Enter the number:\n"))

    Square(Value)

if __name__ == "__main__":
    main()    
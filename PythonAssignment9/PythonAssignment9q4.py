def Cube(No):
    No = No * No * No
    print("Cube of given number is:\n",No)

def main():
    Value = int(input("Enter the number:\n"))

    Cube(Value)

if __name__ == "__main__":
    main()    
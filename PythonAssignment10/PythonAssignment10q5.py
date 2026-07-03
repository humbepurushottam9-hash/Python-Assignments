def Even(No):
    print("Even numbers are:")

    for i in range(1, No + 1):
        if i % 2 != 0:
            print(i)

def main():
    Value = int(input("Enter the number:\n"))

    Even(Value)

if __name__ == "__main__":
    main()
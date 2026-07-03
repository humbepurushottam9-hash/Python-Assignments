def Display(No):
    for i in range(No, 0, -1):
        print(i, end="")

def main():
    Value = int(input("Enter the number:\n"))

    Display(Value)
    
if __name__ == "__main__":
    main()
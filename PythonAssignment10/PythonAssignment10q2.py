def Natural(No):
    Sum = 0
   
    for i in range(1, No + 1):
        Sum = Sum + i

    print("Sum of first", No, "natural numbers is:",Sum)    

def main():
    Value = int(input("Enter the number:\n"))

    Natural(Value)

if __name__ =="__main__":
    main()
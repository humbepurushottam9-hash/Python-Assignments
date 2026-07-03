def Divisible(No):
    if No % 3 == 0 and No % 5 == 0:
        print("Number is divisible by 3 and 5")
    else: 
        print("Number is not divisible by 3 and 5")   

def main():
    Value = int(input("Enter the number:\n"))

    Divisible(Value)

if __name__ == "__main__":
    main()
def Perfect(No):
    Sum = 0

    for i in range(1, No):
        if No % i == 0:
            Sum = Sum + i

    if Sum == No:
        print("Perfect number")
    else:
        print("Not a perfect number")    
        
def main():
    Value = int(input("Enter the number:\n"))

    Perfect(Value)

if __name__ == "__main__":
    main()
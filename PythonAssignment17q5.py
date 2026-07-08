def Prime(No):
    Count = 0

    for i in range(1, No + 1):
        if No % i == 0:
            Count = Count + 1

    if Count == 2:
        print("It is Prime number")
    else:
        print("Not a Prime number")
            
def main():
    Value = int(input("Enter the number:\n"))

    Prime(Value)

if __name__=="__main__":
    main()
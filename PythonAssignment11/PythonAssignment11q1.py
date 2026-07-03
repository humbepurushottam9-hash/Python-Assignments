def Prime(No):
    Count = 0

    for i in range(1, No+1):
        if No % i == 0:
            Count = Count + 1

    if Count == 2:
        print("Number is prime")
    else:
        print("Number is not prime")            
    

def main():
    Value = int(input("Enter the number:\n"))
    Prime(Value)

if __name__ =="__main__":
    main()
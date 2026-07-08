def Addition(No):
    Add = 0

    for i in range(1,No+1):
        if No % i == 0:
            Add = Add + i

    print("Addition is: ",Add)
    
def main():
    Value = int(input("Enter the number:\n"))

    Addition(Value)


if __name__=="__main__":
    main()
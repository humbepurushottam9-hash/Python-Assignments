def Pattern(No):
    for i in range(No):
        for j in range(1, No + 1):
            print(j,end=" ")
        print()    

def main():
    Value = int(input("Enter the number:\n"))

    Pattern(Value)

if __name__=="__main__":
    main()
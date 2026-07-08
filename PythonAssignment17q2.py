def Pattern(No):
    for i in range(No):
        for j in range(No):
            print("*",end = " ")
        print()    
        
def main():
    Value = int(input("Enter the number:\n"))

    Pattern(Value)


if __name__=="__main__":
    main()
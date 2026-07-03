def Count(No):
    Count1 = 0

    while No != 0:
        Count1 = Count1 + 1
        No = No // 10

    print("Number of digits is:",Count1)    


def main():
    Value = int(input("Enter the number:\n"))

    Count(Value)

if __name__ =="__main__":
    main()
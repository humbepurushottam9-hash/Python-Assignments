def Display(No):
    Count = 0

    while No > 0:
        Count = Count + 1
        No = No // 10

    print(Count)
        
def main():
    Value = int(input("Enter the number:\n"))

    Display(Value)

if __name__=="__main__":
    main()
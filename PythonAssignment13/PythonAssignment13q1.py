def Area(No1, No2):
    Ans = No1 * No2
    print("Area of Rectangle is: ",Ans)

def main():
    Value1 = int(input("Enter the length:\n"))
    Value2 = int(input("Enter the width:\n"))

    Area(Value1,Value2)

if __name__=="__main__":
    main()
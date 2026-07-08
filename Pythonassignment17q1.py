import ArithmaticModule

def Arithmatics(No1,No2):
    ArithmaticModule.Addition(No1,No2)
    ArithmaticModule.Substraction(No1,No2)
    ArithmaticModule.Multiplication(No1,No2)
    ArithmaticModule.Division(No1,No2)

def main():
    value1 = int(input("Enter first number: "))
    value2 = int(input("Enter second number: "))

    Arithmatics(value1,value2)

if __name__=="__main__":
    main()
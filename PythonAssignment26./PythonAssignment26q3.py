class Arithmatic:
    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        self.Value1 = int(input("Enter first number: "))
        self.Value2 = int(input("Enter second number: "))

    def Addition(self):
        return self.Value1 + self.Value2

    def Substraction(self):
        return self.Value1 - self.Value2

    def Multiplication(self):
        return self.Value1 * self.Value2

    def Division(self):
        if self.Value2 == 0:
            return "Division by zero is not possible"
        return self.Value1 / self.Value2


def main():
    size = int(input("Enter the number of objects: "))

    for i in range(size):
        print("\nEnter values for Object", i + 1)

        obj = Arithmatic()
        obj.Accept()

        print("Addition :", obj.Addition())
        print("Substraction :", obj.Substraction())
        print("Multiplication :", obj.Multiplication())
        print("Division :", obj.Division())


if __name__ == "__main__":
    main()
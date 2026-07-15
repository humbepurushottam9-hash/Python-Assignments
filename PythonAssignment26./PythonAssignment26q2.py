class Circle:
    PI = 3.14

    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    def Accept(self):
        self.Radius = float(input("Enter the radius: "))

    def CalculateArea(self):
        self.Area = Circle.PI * self.Radius * self.Radius

    def CalculationCircumference(self):
        self.Circumference = 2 * Circle.PI * self.Radius

    def Display(self):
        print("\nRadius :", self.Radius)
        print("Area :", self.Area)
        print("Circumference :", self.Circumference)


def main():
    size = int(input("Enter the number of circles: "))

    for i in range(size):
        print("\nEnter details for Circle", i + 1)

        obj = Circle()
        obj.Accept()
        obj.CalculateArea()
        obj.CalculationCircumference()
        obj.Display()


if __name__ == "__main__":
    main()
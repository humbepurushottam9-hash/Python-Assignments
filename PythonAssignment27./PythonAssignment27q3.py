class Numbers:
    def __init__(self):
        self.Value = int(input("Enter a number: "))

    def ChkPrime(self):
        if self.Value <= 1:
            return False

        for i in range(2, self.Value):
            if self.Value % i == 0:
                return False
        return True

    def ChkPerfect(self):
        Sum = 0

        for i in range(1, self.Value):
            if self.Value % i == 0:
                Sum = Sum + i

        if Sum == self.Value:
            return True
        else:
            return False

    def Factors(self):
        print("Factors are:")
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                print(i, end=" ")
        print()

    def SumFactors(self):
        Sum = 0

        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                Sum = Sum + i

        return Sum


def main():
    obj1 = Numbers()

    print("\nNumber:", obj1.Value)

    if obj1.ChkPrime():
        print("Prime Number")
    else:
        print("Not a Prime Number")

    if obj1.ChkPerfect():
        print("Perfect Number")
    else:
        print("Not a Perfect Number")

    obj1.Factors()
    print("Sum of Factors:", obj1.SumFactors())

    print("\n----------------------\n")

    obj2 = Numbers()

    print("\nNumber:", obj2.Value)

    if obj2.ChkPrime():
        print("Prime Number")
    else:
        print("Not a Prime Number")

    if obj2.ChkPerfect():
        print("Perfect Number")
    else:
        print("Not a Perfect Number")

    obj2.Factors()
    print("Sum of Factors:", obj2.SumFactors())


if __name__ == "__main__":
    main()
class BankAccount:
  
    ROI = 10.5

    def __init__(self, Name, Amount):
        self.Name = Name
        self.Amount = Amount

    def Display(self):
        print("\nAccount Holder :", self.Name)
        print("Current Balance :", self.Amount)

    def Deposit(self):
        DepositAmount = float(input("Enter amount to deposit : "))
        self.Amount = self.Amount + DepositAmount
        print("Amount deposited successfully.")

    def Withdraw(self):
        WithdrawAmount = float(input("Enter amount to withdraw : "))

        if WithdrawAmount <= self.Amount:
            self.Amount = self.Amount - WithdrawAmount
            print("Amount withdrawn successfully.")
        else:
            print("Insufficient balance.")

    def CalculateInterest(self):
        Interest = (self.Amount * BankAccount.ROI) / 100
        return Interest


def main():
    obj1 = BankAccount("Purushottam", 10000)
    obj2 = BankAccount("Radha", 5000)

    print("----- Account 1 -----")
    obj1.Display()

    obj1.Deposit()
    obj1.Display()

    obj1.Withdraw()
    obj1.Display()

    print("Interest :", obj1.CalculateInterest())

    print("\n----- Account 2 -----")
    obj2.Display()

    obj2.Deposit()
    obj2.Display()

    obj2.Withdraw()
    obj2.Display()

    print("Interest :", obj2.CalculateInterest())


if __name__ == "__main__":
    main()
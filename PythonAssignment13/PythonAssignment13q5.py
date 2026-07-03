def DisplayGrade(Marks):
    if Marks >= 90:
        print("Grade: A+")
    elif Marks >= 80:
        print("Grade: A")
    elif Marks >= 70:
        print("Grade: B")
    elif Marks >= 60:
        print("Grade: C")
    else:
        print("Grade: Fail")


def main():
    Value = int(input("Enter the marks:\n"))

    if Value < 0 or Value > 100:
        print("Invalid marks")
        return

    DisplayGrade(Value)


if __name__ == "__main__":
    main()
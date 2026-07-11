from multiprocessing import Pool
import os


def Factorial(No):
    Fact = 1

    for i in range(1, No + 1):
        Fact = Fact * i

    print("Process ID :", os.getpid())
    print("Input Number :", No)
    print("Factorial :", Fact)
    print("-----------------------------")

    return Fact


def main():
    Data = [100, 20, 30, 40]

    p = Pool()

    Result = p.map(Factorial, Data)

    p.close()
    p.join()

    print("Final Result :")
    print(Result)


if __name__ == "__main__":
    main()
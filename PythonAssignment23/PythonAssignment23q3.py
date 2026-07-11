from multiprocessing import Pool
import os


def CountEven(No):
    Count = 0

    for i in range(2, No + 1, 2):
        Count = Count + 1

    print("Process ID :", os.getpid())
    print("Input Number :", No)
    print("Even Numbers Count :", Count)
    print("-----------------------------")

    return Count


def main():
    Data = [1000000, 2000000, 3000000, 4000000]

    p = Pool()

    Result = p.map(CountEven, Data)

    p.close()
    p.join()

    print("Final Result :")
    print(Result)


if __name__ == "__main__":
    main()
from multiprocessing import Pool
import time


def SumPower5(N):
    Sum = 0

    for i in range(1, N + 1):
        Sum = Sum + (i ** 5)

    print("Number :", N)
    print("Sum :", Sum)
    print("------------------------")

    return Sum


def main():
    Data = [1000000, 2000000, 3000000, 4000000]

    StartTime = time.time()

    p = Pool()

    Result = p.map(SumPower5, Data)

    p.close()
    p.join()

    EndTime = time.time()

    print("Final Result :")
    print(Result)

    print("Total Execution Time :", EndTime - StartTime, "seconds")


if __name__ == "__main__":
    main()
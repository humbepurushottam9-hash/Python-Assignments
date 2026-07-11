from multiprocessing import Pool


def ChkPrime(No):
    if No < 2:
        return False

    for i in range(2, int(No ** 0.5) + 1):
        if No % i == 0:
            return False

    return True


def PrimeCount(N):
    Count = 0

    for i in range(1, N + 1):
        if ChkPrime(i):
            Count = Count + 1

    print("Number :", N)
    print("Prime Count :", Count)
    print("---------------------")

    return Count


def main():
    Data = [10000, 20000, 30000, 40000]

    p = Pool()

    Result = p.map(PrimeCount, Data)

    p.close()
    p.join()

    print("Final Result :", Result)


if __name__ == "__main__":
    main()
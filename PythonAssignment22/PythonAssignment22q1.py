from multiprocessing import Pool


def SumSquares(N):
    return (N * (N + 1) * (2 * N + 1)) 


def main():
    Data = [1000000, 2000000, 3000000, 4000000]

    p = Pool()

    Result = p.map(SumSquares, Data)

    p.close()
    p.join()

    print("Input :", Data)
    print("Output:", Result)


if __name__ == "__main__":
    main()
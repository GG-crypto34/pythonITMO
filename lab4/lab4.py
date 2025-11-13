import timeit
import matplotlib.pyplot as plt
from functools import lru_cache

@lru_cache(None)
def rec(i:int)->int:
    if i == 0: return 1
    return rec(i-1)*i

def nonrec(i:int)->int:
    res = 1
    for r in range(1,i+1):
        res = res * r
    return res

def benchmark(func, n, number = 1, repeat = 5, type1 = "nv")->float:
    total = 0
    if type1 == "v":
        for i in range(0,n,10):
            time = timeit.repeat(lambda: func(i), number=number, repeat=repeat)
            total += min(time)
        if n == 0: return total
        return total / n
    else:
        time = timeit.repeat(lambda: func(n), number=number, repeat=repeat)
    return min(time)

def main():

    reqTest = []
    nonreqTets = []
    test_data = list(range(0, 500, 10))

    for n in test_data:
        nonreqTets.append(benchmark(nonrec, n,number = 1000, repeat=5, type1 = "nv"))
        reqTest.append(benchmark(rec, n,number = 1000, repeat=5, type1 = "nv"))

    plt.plot(test_data, reqTest, label="Рекурсивный")
    plt.plot(test_data, nonreqTets, label="Итеративный")
    plt.xlabel("n")
    plt.ylabel("Время (сек)")
    plt.yscale("log", base = 2)
    plt.legend()
    plt.title("Сравнение рекурсивного и итеративного факториала")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
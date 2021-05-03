def rec(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return rec(n - 1) + rec(n - 2)


def main():
    n = int(input('Zadejte pocet prvku Fib. posl.: '))
    fib_seq = []
    # for num in range(n + 1):
    #     fib_seq.append(rec(num))

    fib_seq = [rec(num) for num in range(n + 1)]
    print(fib_seq)


if __name__ == '__main__':
    main()

import time


def is_prime_1(p):
    if p <= 1:
        return False

    # all possibile divisors
    for d in range(2, p):
        if p % d == 0:
            return False
    return True


def is_prime_2(p):
    if p <= 1:
        return False
    if p == 2:
        return True
    if p % 2 == 0:
        return False

    # odd divisors up to sqrt(p)
    limit = int(p ** 0.5)
    for d in range(3, limit + 1, 2):
        if p % d == 0:
            return False
    return True


def time_func(inp, fun):
    start = time.time()
    res = fun(inp)
    end = time.time()
    delta = end - start
    return res, delta


def sleep_one(_):
    time.sleep(1)
    return False


def main():
    # print(time_func(1, sleep_one))

    print(time_func(433494437, is_prime_2))
    print(time_func(433494437, is_prime_1))


if __name__ == '__main__':
    main()

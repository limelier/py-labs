from typing import List


def fib_n(n: int) -> List[int]:
    if n <= 0:
        return []

    nums = [0, 1]
    if n <= 2:
        return nums[:n-1]

    for i in range(2, n):
        nums.append(nums[-1] + nums[-2])
    return nums


if __name__ == '__main__':
    print(fib_n(-1), fib_n(1), fib_n(2), fib_n(20))

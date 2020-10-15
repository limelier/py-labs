# find the GCD of multiple numbers read from the console
from typing import List


def gcd_pair(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a


def gcd_list(nums: List[int]) -> int:
    gcd = gcd_pair(nums[0], nums[1])
    for num in nums[2:]:
        gcd = gcd_pair(gcd, num)
    return gcd


def gcd_many():
    nums = [int(num_str) for num_str in input().split(' ')]
    gcd = gcd_list(nums)
    print(gcd)


if __name__ == '__main__':
    gcd_many()

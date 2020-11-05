from typing import List


def num_pairs(nums: List[int]):
    """
    Receive nums, a list of ints which contains as many odd numbers as it does even.
    Return a list of tuples containing corresponding number pairs.
    """
    odds = [num for num in nums if num % 2 == 1]
    evens = [num for num in nums if num % 2 == 0]
    return list(zip(odds, evens))


if __name__ == '__main__':
    print(num_pairs([1, 2, 3, 4, 5, 6, 7, 8]))

from collections import Counter
from typing import Hashable, List


def x_occurrences(x: int, *lists: List[Hashable]) -> List[Hashable]:
    """
    Filters the items in a number of lists to only those which appear exactly x times.
    """
    flat_list = [item for sublist in lists for item in sublist]
    return [k for k, v in Counter(flat_list).items() if v == x]


if __name__ == '__main__':
    print(x_occurrences(
        2,
        [1, 2, 3],
        [2, 3, 4],
        [4, 5, 6],
        [4, 1, 'test']
    ))

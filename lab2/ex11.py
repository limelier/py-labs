from typing import List, Tuple


def ordered(tuple_list: List[Tuple[str, str]]) -> List[Tuple[str, str]]:
    """
    Get a copy of a list of string tuples ordered by the third character of the second element.
    """
    return sorted(tuple_list, key=lambda t: t[1][2])


if __name__ == '__main__':
    tuples = [('abc', 'bcd'), ('abc', 'zza')]
    print(ordered(tuples))

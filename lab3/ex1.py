from typing import List, Any, Tuple, Set


def list_sets(list_1: List[Any], list_2: List[Any]) -> Tuple[Set[Any], Set[Any], Set[Any], Set[Any]]:
    set_1 = set(list_1)
    set_2 = set(list_2)
    return set_1 & set_2, set_1 | set_2, set_1 - set_2, set_2 - set_1


def main():
    list_1 = [1, 3, 5, 7, 9, 11, 13, 15]
    list_2 = [2, 3, 5, 7, 11, 13, 17, 19]
    intersection, reunion, difference_1, difference_2 = list_sets(list_1, list_2)
    print(intersection)
    print(reunion)
    print(difference_1)
    print(difference_2)


if __name__ == '__main__':
    main()

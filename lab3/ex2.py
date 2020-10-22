from collections import Counter
from typing import Dict


def dict_way(string: str) -> Dict[str, int]:
    occurrences: dict = {}

    for character in string:
        occurrences[character] = occurrences.setdefault(character, 0) + 1

    return occurrences


def counter_way(string: str) -> Dict[str, int]:
    return dict(Counter(string))


def main():
    string = 'Ana has apples.'
    print(dict_way(string))
    print(counter_way(string))


if __name__ == '__main__':
    main()

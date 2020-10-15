from string import ascii_lowercase
from collections import Counter


def most_common_letter_naive(string: str) -> str:
    occurrences = [(string.lower().count(char), char) for char in ascii_lowercase]
    return max(occurrences)[1]


def most_common_letter(string: str) -> str:
    letters = [a for a in string.lower() if a in ascii_lowercase]
    best, _ = Counter(letters).most_common(1)[0]
    # it's also possible to count letters manually in a dictionary, but Counter is probably more efficient
    return best


if __name__ == '__main__':
    print(most_common_letter('an apple is not a tomato'))

def count(source: str, substring: str) -> int:
    return source.count(substring)


def count_overlapping_simple(source: str, substring: str) -> int:
    occurrences: int = 0
    size = len(substring)
    # all_substrings = [source[i:i+size] for i in range(0, len(source) - size + 1)]
    for i in range(0, len(source) - size + 1):
        if source[i:i+size] == substring:
            occurrences += 1
    return occurrences


def count_overlapping(source: str, substring: str) -> int:
    size = len(substring)
    all_substrings = [source[i:i+size] for i in range(0, len(source) - size + 1)]
    return all_substrings.count(substring)


def count_overlapping_2(source: str, substring: str) -> int:
    occurrences: int = 0
    pos = 0
    while True:
        pos = source.find(substring, pos) + 1
        if pos == 0:
            break
        occurrences += 1
    return occurrences


if __name__ == '__main__':
    print(count_overlapping_2("aaaaa", "aaa"))

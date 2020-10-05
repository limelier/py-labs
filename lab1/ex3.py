def count(source: str, substring: str) -> int:
    return source.count(substring)


def count_overlapping(source: str, substring: str) -> int:
    occurences = 0
    size = len(substring)
    all_substrings = [source[i:i+size] for i in range(0, len(source) - size + 1)]
    return all_substrings.count(substring)


if __name__ == '__main__':
    print(count_overlapping("aaaaa", "aaa"))

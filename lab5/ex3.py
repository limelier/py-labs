vowels = set('aeiou')


def vowels_naive(string: str):
    vowel_list = []
    for c in string:
        if c in vowels:
            vowel_list.append(c)
    return vowel_list


def vowels_list_comprehension(string: str):
    return [c for c in string if c.lower() in vowels]


def vowels_filter_lambda(string: str):
    return list(filter(lambda c: c.lower() in vowels, string))


def main():
    string = 'Programming in Python is fun'
    print(vowels_list_comprehension(string))
    print(vowels_filter_lambda(string))
    print(vowels_naive(string))


if __name__ == '__main__':
    main()

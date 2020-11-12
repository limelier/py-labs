import re


def match_any(strings, patterns):
    regexes = [re.compile(pattern) for pattern in patterns]
    return [
        string
        for string in strings
        if any(
            regex.match(string)
            for regex in regexes
        )
    ]


if __name__ == '__main__':
    strs = ['hello', '123', 'goodbye', '     ']
    pats = [r'[a-g]+', r'\d+']
    print(match_any(strs, pats))

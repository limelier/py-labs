import re


def match_of_len(pattern, text, length):
    # will not work for overlapping matches!
    matches = re.findall(pattern, text)
    return [match for match in matches if len(match) == length]


def substr_which_match(pattern, text, length):
    reg = re.compile(pattern)
    return [
        substr
        for substr in [
            text[i:i+length]
            for i in range(0, len(text) - length + 1)
        ]
        if reg.match(substr)
    ]


if __name__ == '__main__':
    sentence = 'Hello there four letter word fans!'
    print(substr_which_match(r'\w{4}', sentence, 4))

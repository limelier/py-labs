import re

re_word = re.compile(r'\w+')


def words(string: str):
    return re_word.findall(string)


if __name__ == '__main__':
    sentence = 'Hello, this is my 1st sentence idea. E_n_j_o_y!'
    print(words(sentence))

from os import path, walk, SEEK_END, SEEK_SET
from collections import Counter


def f(my_path):
    # if file, print last 20 characters
    if path.isfile(my_path):
        with open(my_path, "r") as file:
            # find last position in file
            file.seek(0, SEEK_END)
            # go to 20 characters before that, if possible
            file.seek(max(0, file.tell() - 20), SEEK_SET)
            return file.read(20)
    # if directory, return a frequency list of extensions of files in
    # directory
    else:
        counter = Counter(
            path.splitext(file)[1].lstrip('.')
            for _, _, files in walk(my_path)
            for file in files
        )
        freq_list = list(counter.items())
        return sorted(freq_list, key=lambda item: item[1], reverse=True)


def main():
    print(f('/home/limelier/.config/alacritty/alacritty.yml'))
    print(f('./short.txt'))
    print(f('/home/limelier/.config'))


if __name__ == '__main__':
    main()

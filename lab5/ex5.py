def filter_nums(things):
    # return [item for item in things if type(item) in {int, float, complex}]
    return [item for item in things if isinstance(item, (int, float, complex))]


if __name__ == '__main__':
    print(filter_nums([1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0, complex(2, 2)]))

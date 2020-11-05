def add_keywords(*_, **nums):
    return sum(nums.values())


def main():
    print(add_keywords(1, 2, a=3, b=4))
    add_kw = lambda *_, **nums: sum(nums.values())
    print(add_kw(1, 2, a=3, b=4))


if __name__ == '__main__':
    main()

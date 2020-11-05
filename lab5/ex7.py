def fib_n(n):
    if n < 1:
        return []
    elif n == 1:
        return [0]
    else:
        nums = [0, 1]
        for i in range(2, n):
            nums.append(nums[-1] + nums[-2])
        return nums


# def fib(filters=None, offset=None, limit=None):
def fib(**kwargs):
    nums = fib_n(1000)

    filters = kwargs.get('filters')
    if filters is not None:
        nums = [num for num in nums if all(f(num) for f in filters)]
        # new_nums = []
        # for num in nums:
        #     good = True
        #     for f in filters:
        #         if not f(num):
        #             good = False
        #             break
        #     if good:
        #         new_nums.append(num)
        # nums = new_nums

    offset = kwargs.get('offset')
    if offset is not None:
        nums = nums[offset:]

    limit = kwargs.get('limit')
    if limit is not None:
        nums = nums[:limit]

    return nums


if __name__ == '__main__':
    print(fib_n(20))
    print(fib(
        filters=[
            lambda item: item % 2 == 0,
            lambda item: item % 3 == 0,
        ],
        limit=2,
        offset=2
    ))

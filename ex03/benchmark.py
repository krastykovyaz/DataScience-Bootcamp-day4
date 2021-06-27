#!/usr/bin/env python
import timeit
import sys
from functools import reduce


def loop_sum(number):
    total = 0
    for i in range(number + 1):
        total += i ** 2
    return total


def reduce_sum(number):
    return reduce(lambda acum, x: acum + x ** 2, range(number + 1))


def main():
    if len(sys.argv) != 4:
        sys.exit()
    func_name = sys.argv[1]
    try:
        repeat_count = int(sys.argv[2])
        number = int(sys.argv[3])
    except ValueError:
        sys.exit()
    mapping_func = {'loop': loop_sum, 'reduce': reduce_sum}
    if func_name not in mapping_func:
        sys.exit()
    print(timeit.timeit(lambda: mapping_func[func_name](number), number=repeat_count))


if __name__ == '__main__':
    main()
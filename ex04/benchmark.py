#!/usr/bin/env python
import timeit
import random
from collections import Counter


def count_numbers(numbers):
    numbers_dict = {}
    get = numbers_dict.get
    for number in numbers:
        numbers_dict[number] = get(number, 0) + 1
    return numbers_dict


def most_common(numbers, count=10):
    return dict(sorted(count_numbers(numbers).items(), reverse=True,
                       key=lambda x: x[1])[:count])


def main():
    random_numbers = [random.randint(0, 100) for _ in range(1_000_000)]
    Counter(random_numbers)
    my_func_time = timeit.timeit(lambda: count_numbers(random_numbers), number=1)
    counter_time = timeit.timeit(lambda: dict(Counter(random_numbers)), number=1)
    my_top_time = timeit.timeit(lambda: most_common(random_numbers), number=1)
    counter_top_time = timeit.timeit(
        lambda: dict(Counter(random_numbers).most_common()[:10]), number=1)
    print(f'''my function: {my_func_time}
Counter: {counter_time}
my top: {my_top_time}
Counter's top: {counter_top_time}''')


if __name__ == '__main__':
    main()
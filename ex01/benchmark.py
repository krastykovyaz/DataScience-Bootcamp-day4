#!/usr/bin/env python
import timeit


def get_gmails_loop(mails):
    result_mails = []
    for mail in mails:
        if mail.endswith('@gmail.com'):
            result_mails.append(mail)
    return result_mails


def get_gmails_lc(mails):
    return [mail for mail in mails if mail.endswith('@gmail.com')]


def get_gmails_map(mails):
    return list(map(lambda mail: mail.endswith('@gmail.com'), mails))


def main():
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com'] * 5
    repeat_count = 90_000_000
    lc_time = timeit.timeit(lambda: get_gmails_lc(emails), number=repeat_count)
    loop_time = timeit.timeit(lambda: get_gmails_loop(emails), number=repeat_count)
    map_time = timeit.timeit(lambda: get_gmails_map(emails), number=repeat_count)
    if lc_time < loop_time and lc_time < map_time:
        print('it is better to use a list comprehension')
    elif loop_time < lc_time and loop_time < map_time:
        print('it is better to use a loop')
    else:
        print('it is better to use a map')
    print('{} vs {} vs {}'.format(*sorted([lc_time, loop_time, map_time])))


if __name__ == '__main__':
    main()

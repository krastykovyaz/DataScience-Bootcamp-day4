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


def main():
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com'] * 5
    repeat_count = 90_000_000
    lc_time = timeit.timeit(lambda: get_gmails_lc(emails), number=repeat_count)
    loop_time = timeit.timeit(lambda: get_gmails_loop(emails), number=repeat_count)
    if lc_time < loop_time:
        print('it is better to use a list comprehension')
    else:
        print('it is better to use a loop')
    print('{} vs {}'.format(*sorted([lc_time, loop_time])))


if __name__ == '__main__':
    main()

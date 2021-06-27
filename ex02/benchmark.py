#!/usr/bin/env python
import timeit
import sys


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


def get_gmails_filter(mails):
    return list(filter(lambda mail: mail.endswith('@gmail.com'), mails))


def main():
    mapping_func = {'loop': get_gmails_loop, 'list_comprehension': get_gmails_lc,
                    'map': get_gmails_map, 'filter': get_gmails_filter}
    if len(sys.argv) != 3:
        sys.exit()
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com'] * 5
    repeat_count = sys.argv[2]
    func_name = sys.argv[1]
    if not repeat_count.isdecimal() or func_name not in mapping_func:
        sys.exit()
    repeat_count = int(repeat_count)
    print(timeit.timeit(lambda: mapping_func[func_name](emails), number=repeat_count))


if __name__ == '__main__':
    main()

#!/usr/bin/env python
import sys
import resource


def read_whole_file(filename):
    with open(filename) as f:
        return f.readlines()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit()
    try:
        for row in read_whole_file(sys.argv[1]):
            pass
        resource_data = resource.getrusage(resource.RUSAGE_SELF)
        max_memory = round(resource_data.ru_maxrss / 2 ** 30, 3)
        script_time = round(resource_data.ru_utime + resource_data.ru_stime, 2)
        print(f'Peak Memory Usage = {max_memory} GB')
        print(f'User Mode Time + System Mode Time = {script_time}s')
    except FileNotFoundError:
        print(f'File "{sys.argv[1]}" not found')
        sys.exit()
    except:
        sys.exit()

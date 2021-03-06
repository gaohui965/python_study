#!/usr/bin/env python

import sys

def binary_search(a, m):
    low = 0
    high = len(a) - 1
    while (low <= high):
        mid = (low + high) / 2
        midval = a[mid]

        if midval < m:
            low = mid + 1
        elif midval > m:
            high = mid - 1
        else:
            print mid
            return mid
    print -1
    return -1

if __name__ == "__main__":
    a = [int(i) for i in list(sys.argv[1])]
    m = int(sys.argv[2])
    binary_search(a, m)

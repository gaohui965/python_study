#!/usr/bin/env python

import sys

def usage():
    print("Usage: %s [search_list] [search_num]" %sys.argv[0])

def binary_search(search_list, search_num):
    low = 0
    high = len(search_list) - 1
    while (low <= high):
        mid_index = (low + high) / 2
        midval = search_list[mid_index]
        if midval < search_num:
            low = mid_index + 1
        elif midval > search_num:
            high = mid_index - 1
        else:
            print mid_index
            return mid_index
   
    print -1
    return -1

def main():
    if len(sys.argv) != 3:
        usage()
        exit(-1)
    search_list = [int(i) for i in list(sys.argv[1])]
    search_num = int(sys.argv[2])
    binary_search(search_list, search_num)

if __name__ == "__main__":
    main()

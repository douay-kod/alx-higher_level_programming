#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    l = list(a_dictionary.keys())
    l.sort()

    for i in l:
        print("{}: {}".format(i, a_dictionary.get(i)))

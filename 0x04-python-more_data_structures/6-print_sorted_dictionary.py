#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    l = list(a_dictionary.key(s))
    l.sort()
    
    for i in range(len(l)):
        print("{}: {}".format(l[i], a_dictionary.get(i)))

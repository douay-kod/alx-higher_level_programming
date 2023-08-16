#!/usr/bin/python3
def uniq_add(my_list=[]):
    n_l = set(my_list)
    n=0

    for i in n_l:
        n += i
    return n

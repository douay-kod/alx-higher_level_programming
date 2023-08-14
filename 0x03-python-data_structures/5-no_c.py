#!/usr/bin/python3
# 5-no_c.py


def no_c(my_string):
    """Remove all characters c and C from a string."""
    copy=""
    for i in my_string:
        if i!="c" and i!="C":
            copy+=i
    return copy

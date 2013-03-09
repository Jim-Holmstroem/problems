#do mul/div and sub from addition only for integers

import itertools as it
import functools as ft

def mul(a, b):
    return sum(it.repeat(a, b))
def div(m, n):
    assert(n!=0)
    return len(range(m, 0, -n))
def sub(a, b):
    return a+(~b+1) #~x = -x-1 


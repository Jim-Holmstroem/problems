from __future__ import print_function
import itertools as it
import functools as ft
from functools import partial, reduce
import operator as op
import heapq

def unpack(f,a):
    return f(*a)
def unpackd(f,a):
    return f(**a)

def accumulate(iterable, func=op.add):
    it = iter(iterable)
    total = next(it)
    yield total
    for element in it:
        total = func(total, element)
        yield total

def tee(a):
    print(a)
    return a

def render_heap(heap, heap_width=128):
    # k->(2k+1,2k+2)
    largest_element = len(max(map(str,heap), key=len))

    def render_heap_from_level(heap, k): #O(log(n)) so okay
        max_width = 2**k
        first_level, rest = heap[:max_width], heap[max_width:] 
        print(
            " ".join(
                map(
                    "[{0}]".format,
                    map(
                        op.methodcaller('rjust', largest_element),    
                        map(
                            str,
                            first_level
                        )
                    )
                )
            )
        )
        if(rest):
            render_heap_from_level(rest, k+1)
    
    render_heap_from_level(heap, 0)

def median(*x):
    if(len(x)==0):
        raise Exception()
    sortedx = sorted(x)
    lengthx = len(sortedx)
    if not lengthx % 2:
        return float(sortedx[lengthx // 2] + sortedx[lengthx // 2 - 1]) / 2
    return sortedx[lengthx // 2]


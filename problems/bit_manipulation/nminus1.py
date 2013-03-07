from __future__ import print_function

#What does (n&(n-1))==0 do?
#
#for n not equal 0
#    xxx10...0-1=xxx01...1
#    xxx10...0&xxx01...1 = xxx00...0
#    and this is ==0 if and only if xxx=0
#    this gives us that the 
#    expression is true if and only if bitcount(n)==1 or eqv. n=2^i
#
#for n == 0
#    then (000&111)==0
#    which is bitcount(n)==0
#
#Conclusion:
#    the expression checks if the bitcount(n) \in {0,1}
#

from ctypes import c_uint64
from random import randrange
import functools as ft
import itertools as it
import operator as op
from utils import composition

def nminus1(n):
    return (n.value&(n.value-c_uint64(1).value)==0) 

positive_tests = set(
    [0,]+list(map(lambda i: 1<<i, range(63)))
)

negative_tests= set(
    range(2**16)
)-positive_tests

print("Test:pos={postest} and neg={negtest}".format(
    postest=all(
        map(
            composition(nminus1, c_uint64),
            positive_tests
        )
    ),
    negtest=not any(
        map(
            composition(nminus1, c_uint64),
            negative_tests
        )
    )
))

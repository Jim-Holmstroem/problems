
from collections import Counter
import operator as op
import functools as ft
import itertools as it
import utils

def simple_words_permutated(*word):
    """
    Counter is basically an accumulated hashmap, 
    and for a finit list to be permutations of each other
    <==> the count of each symbol is the same 
    (that is we have one-to-one correlation)
    """
    return utils.equal(
        *map(
            Counter,
            word
        )
    )




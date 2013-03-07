import functools as ft
import string

#how bit is the numbers? atleast 64
mask_odd = 0x5555555555555555 #0101
mask_even= mask_odd<<1
clip64bit= 0xFFFFFFFFFFFFFFFF

def bit_swap64(a):
    #clipping of ones higher then position 64 is needed in python, but not if the datatype was actual int64
    return (
        (a>>1)
        &
        mask_odd
    )|(
        (
            clip64bit
            &
            (a<<1)
        )
        &
        mask_even
    )

def test(a):
    a_bin, a_swap_bin = bin(a), bin(bit_swap64(a))
    a_bin, a_swap_bin = map(
        ft.partial(
            string.rjust,
            width=max(map(len, [a_bin, a_swap_bin]))
        ),
        [
            a_bin,
            a_swap_bin
        ]
    )
    print(a_bin)
    print(a_swap_bin)
    print("="*32)

import random
def random64():
    while(True):
        yield random.getrandbits(64)

rndm = random64()
list(
    map(
        test, 
        map(
            lambda x: next(rndm), 
            range(128)
        )
    )
)



#how bit is the numbers? atleast 64
mask_odd = 0x55555555 #0101
mask_even= mask_odd<<1
clip64bit= 0xFFFFFFFF

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


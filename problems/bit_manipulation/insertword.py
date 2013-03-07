
import itertools as it

def insert_word(a, b, i, j):
    maskj=(1<<j+1)-1
    maski=(1<<i+1-1)-1 #one less since exclusive
    mask = maskj&~maski
    saved_or_zero = a & ~mask #where ~mask is one it saves the value from a else always zero
    b_moved = b<<i
    return saved_or_zero|b_moved

#PROBLEM: insert word b at position i (to j) on a.

print(list(it.starmap(
    lambda a,b,i,j: bin(insert_word(a,b,i,j)),
    [
        (0b1000000000,0b10011,2,6),
        (0b1010101010,0b10011,2,6),
        (0b1000000000,0b10011,1,5),
        (0b1000000000,0b10011,0,4),
    ]
)))

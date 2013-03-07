import itertools as it

def simple_compression(word):
    compressed = ''.join(
        map(
            ''.join,
            ( map(str,[k,len(list(v))]) for k, v in it.groupby(word))
        )
    )
    if(len(compressed)<len(word)):
        return compressed
    else:
        return word

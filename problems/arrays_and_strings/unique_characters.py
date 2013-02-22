
def simple_unique_characters(word):
    """
    set is basically a hashmap with (key, True) pairs,
    basically just marking existence.
    """
    return len(set(word)) == len(word)



def simple_unique_characters(word):
    """set is basically a hashmap with (key, True) pairs, key must be hashable
    """
    return len(set(word)) == len(word)


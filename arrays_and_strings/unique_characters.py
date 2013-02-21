
def simple_unique_characters(word):
    """set is a hashmap with (key,key) pairs, key must be hashable
    """
    return len(set(word)) == len(word)


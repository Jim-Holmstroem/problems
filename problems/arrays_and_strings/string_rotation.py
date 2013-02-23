
import itertools as it

#check if a two strings is rotation of each other. 
#ex: "hello world" and "llo worldhe", using only one call to isSubstring

# isSubstring: "ll" in "hello"
# isSubstring: "hello".find("ll")!=-1

def isRotation(s1, s2):
    #you have one unknown variable and that is the 'start' position
    #trivial search would be O(N*string_equal) = O(N^2)

    #if both words are the same length and you double word A then B in AA
    #if this is true it exists an rotated offset between them and they are thus 
    #guarenteed to be rotations of each other
    #this is O(N+isSubString) where isSubString either is O(N) worstcase with a KMP or O(N^2) with trivial.
    #which one of these is the fastest one most benchmark to see since the distribution of characters and 
    #the distribution of the length of the words affect the running time.

    return len(s1)==len(s2) and s1 in s2*2

print(all(
    (
        isRotation("hello","elloh"),
        not isRotation("hbllo","elloh"),
        isRotation("heheo","eheoh"),
        not isRotation("hello","h"),
        not isRotation("h","elloh"),
        isRotation("bobobo","obobob"),
        isRotation("saxxsa","sasaxx"),
        isRotation("s","s"),
        isRotation("",""),
    )
))

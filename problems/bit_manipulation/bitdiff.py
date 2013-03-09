from utils import bitcount

def bitdiff(a, b):
    #count the number of bit flips required to go from a to b
    return bitcount(a^b) #count the bits that differs

testcases = [
    ([ 0b101, 0b010], 3),
    ([ 0b110, 0b011], 2),
    ([0b1101,0b0110], 3),
]+list(map(
    lambda x: ([(1<<x)-1, 0b0], x), #all against nothing
    range(128)
))+list(map(
    lambda x: ([x, 0b0], bitcount(x)), #against zero
    range(4096)
))+list(map(
    lambda x: ([x, x], 0), #id cases
    range(4096)
))

def test(testcase):
    return bitdiff(testcase[0][0], testcase[0][1]) == testcase[1] 
def symmetric_test(testcase): #bitdiff(a,b)==bitdiff(b,a)
    return bitdiff(testcase[0][1], testcase[0][0]) == testcase[1] 

print(
    all(
        map(
            test,
            testcases
        )
    )
)
print(
    all(
        map(
            symmetric_test,
            testcases
        )
    )
)


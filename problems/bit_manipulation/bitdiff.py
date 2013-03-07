from utils import bitcount

def bitdiff(a, b):
    #count the number of bit flips required to go from a to b
    return bitcount(a^b) #count the bits that differs

testcases = [
    ([0b1,0b0],1),
]+list(map(
    lambda x: ([x, x], 0), #id cases
    range(32)
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


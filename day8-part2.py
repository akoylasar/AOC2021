import time
import re
from collections import Counter
# from multiprocessing.dummy import Pool as ThreadPool

'''
p1. a, c 8
b 6
p2. d, g 7
e 4
f 9

quickly map b, e, f
then based on "1" map c
then use p1 to map a
use "4" to map d
use p2 to map g
'''
segmentValues = {'a': 1, 'b': 2, 'c': 4, 'd': 8, 'e': 16, 'f': 32, 'g': 64}

# precalculated based on the mapping above and getValue function
digitValueMap = {119: 0, 36: 1, 93: 2, 109: 3, 46: 4, 107: 5, 123: 6, 37: 7, 127: 8, 111: 9}

def solve(lines):
    nput = [re.split(r"\s*[\\|\s]\s*", l.strip()) for l in lines]
    sums = [decodeAndSum(s) for s in nput]
    # pool = ThreadPool(4) # roughly @0.033s by comparison single threaded version is roughly @0.006s
    # sums = pool.map(decodeAndSum, nput)
    print(sum(sums))

def decodeAndSum(nput):
    mapping = getMapping(nput[:10])
    segmentGroups = [''.join([mapping[digit] for digit in nput[i]]) for i in range(10, 14)]
    digits = [digitValueMap[getSegmentGroupValue(seg)] for seg in segmentGroups]
    return digits[0] * 1000 + digits[1] * 100 + digits[2] * 10 + digits[3]

def getMapping(nput):
    charCnt = Counter(''.join(nput)).most_common()
    def getChar(count):
        res = []
        for x in charCnt:
            if x[1] == count:
                res.append(x[0])
        return res
    # map b, e, f
    mapping = {}
    b = getChar(6)[0]
    e = getChar(4)[0]
    f = getChar(9)[0]
    mapping[b] = 'b'
    mapping[e] = 'e'
    mapping[f] = 'f'

    # map c
    one = list([s for s in nput if len(s) == 2][0])
    one.remove(f)
    c = one[0]
    mapping[c] = 'c'

    # map a
    ac = getChar(8)
    ac.remove(c)
    mapping[ac[0]] = 'a'

    # map d
    four = list([s for s in nput if len(s) == 4][0])
    four.remove(b)
    four.remove(c)
    four.remove(f)
    d = four[0]
    mapping[d] = 'd'

    # map g
    dg = getChar(7)
    dg.remove(d)
    mapping[dg[0]] = 'g'

    return mapping

def getSegmentGroupValue(segmentGroup):
    res = 0
    for seg in segmentGroup:
        res |= segmentValues[seg]
    return res

if __name__ == '__main__':
    # original = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']
    # mapped = [getSegmentGroupValue(seg) for seg in original]
    with open('day8.txt', 'r') as file:
        lines = file.readlines()
    start = time.time()
    solve(lines)
    print("%s seconds" % (time.time() - start))
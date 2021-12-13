import numpy as np
import time

def solve(nput):
    input = np.array([[int(s) for s in line.strip("\n")] for line in nput])
    print(getLifeSupportRating(input))

def getLifeSupportRating(input):
    o2GeneratorRating = getRating(input[:], lambda a : int(sum(a) >= len(a) / 2))
    co2ScrubberRating = getRating(input[:], lambda a : int(sum(a) < len(a) / 2))
    return o2GeneratorRating * co2ScrubberRating

def getRating(input, criteriaFunc):
    i = 0
    while len(input) > 1:
        pattern = criteriaFunc(input[0:, i])
        input = np.array([x for x in input if x[i] == pattern])
        i += 1
    return sum(x * (1 << (len(input[0]) - i - 1)) for i, x in enumerate(input[0]))

if __name__ == '__main__':
    with open('day3.txt', 'r') as file:
        nput = file.readlines()
    start = time.time()
    solve(nput)
    print("%s seconds" % (time.time() - start))
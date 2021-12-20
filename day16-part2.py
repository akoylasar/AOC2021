import time
from functools import reduce

def readLiteralPacket(seq, i):
    l = []
    # print("I am a literal packet at " + str(i))
    while True:
        l.append(seq[i + 1: i + 5])
        if seq[i] == '0':
            break
        i += 5
    i += 5
    literal = int(''.join(l), 2)
    return i, literal

def readOperatorPacket(seq, i, counter, typeId):
    lengthTypeId = int(seq[i])
    i += 1
    literals = []
    if lengthTypeId:
        numSubPackets = int(seq[i: i + 11], 2)
        # print("I am an operator packet at " + str(i) + " with " + str(numSubPackets) + " sub packets")
        i += 11
        for j in range(numSubPackets):
            i, literal = readPacket(nput, i, counter)
            literals.append(literal)
    else:
        totalLengthInBits = int(seq[i: i + 15], 2)
        # print("I am an operator packet at " + str(i) + " with total length of " + str(totalLengthInBits) + " bits")
        i += 15
        j = i
        while True:
            j, literal = readPacket(nput, j, counter)
            literals.append(literal)
            if j - i == totalLengthInBits:
                i = j
                break
    return i, literals

def readPacket(nput, i, counter):
    version = int(nput[i: i + 3], 2)
    i += 3
    counter[0] += version
    typeId = int(nput[i: i + 3], 2)
    i += 3
    literal = None
    if typeId == 4:  # literal packet
        i, literal = readLiteralPacket(nput, i)
    else: # operator packet
        i, literals = readOperatorPacket(nput, i, counter, typeId)
        if typeId == 0: # sum
            literal = sum(literals)
        elif typeId == 1: # mul
            literal = reduce(lambda a, b: a * b, literals)
        elif typeId == 2: # min
            literal = min(literals)
        elif typeId == 3: # max
            literal = max(literals)
        elif typeId == 5: # gt
            literal = literals[0] > literals[1]
        elif typeId == 6: # lt
            literal = literals[0] < literals[1]
        elif typeId == 7: # eq
            literal = literals[0] == literals[1]
    return i, literal

def solve(nput):
    i, result = readPacket(nput, i=0, counter=[0])
    print(result)

if __name__ == '__main__':
    with open('day16.txt', 'r') as file:
        s = file.readline().strip()
        nput = [bin(int(x, 16))[2:].zfill(4) for x in s]
        nput = ''.join(nput)
    start = time.time()
    solve(nput)
    print("%s seconds" % (time.time() - start))
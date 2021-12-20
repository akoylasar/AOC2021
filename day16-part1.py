import time

def readLiteralPacket(seq, i):
    # print("I am a literal packet at " + str(i))
    while True:
        if seq[i] == '0':
            break
        i += 5
    i += 5
    return i

def readOperatorPacket(seq, i, counter):
    lengthTypeId = int(seq[i])
    i += 1
    if lengthTypeId:
        numSubPackets = int(seq[i: i + 11], 2)
        # print("I am an operator packet at " + str(i) + " with " + str(numSubPackets) + " sub packets")
        i += 11
        for j in range(numSubPackets):
            i = readPacket(nput, i, counter)
    else:
        totalLengthInBits = int(seq[i: i + 15], 2)
        # print("I am an operator packet at " + str(i) + " with total length of " + str(totalLengthInBits) + " bits")
        i += 15
        j = i
        while True:
            j = readPacket(nput, j, counter)
            if j - i == totalLengthInBits:
                i = j
                break
    return i

def readPacket(nput, i, counter):
    version = int(nput[i: i + 3], 2)
    i += 3
    counter[0] += version
    typeId = int(nput[i: i + 3], 2)
    i += 3
    if typeId == 4:  # literal packet
        i = readLiteralPacket(nput, i)
    else: # operator packet
        i = readOperatorPacket(nput, i, counter)
    return i

def solve(nput):
    counter = [0]
    i = 0 # packet counter
    readPacket(nput, i, counter)
    print(counter[0])

if __name__ == '__main__':
    with open('day16.txt', 'r') as file:
        s = file.readline().strip()
        nput = [bin(int(x, 16))[2:].zfill(4) for x in s]
        nput = ''.join(nput)
    start = time.time()
    solve(nput)
    print("%s seconds" % (time.time() - start))
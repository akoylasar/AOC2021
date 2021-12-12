import time

# TODO: try to see if you can go lower with the execution time
def solve(nput):
    fishBin = [0] * 9
    for i in nput:
        fishBin[int(i)] += 1
    for i in range(256):
        newFishCnt = fishBin[0]
        for j in range(1, 9):
            fishBin[j - 1] = fishBin[j]
        fishBin[6] += newFishCnt
        fishBin[8] = newFishCnt
    print(sum(fishBin))

if __name__ == '__main__':
    with open('day6.txt', 'r') as file:
        nput = file.readline().strip().split(',')
    start = time.time()
    solve(nput)
    print("%s seconds" % (time.time() - start))

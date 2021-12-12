def solve():
    input = open('day1.txt', 'r')
    depthList = []
    for line in input:
        depthList.append(int(line))
    print(coutDepthIncreases(depthList))

def coutDepthIncreases(depthList):
    count = 0
    for i in range(len(depthList) - 1):
        count += 1 if((depthList[i + 1] - depthList[i]) > 0) else 0
    return count

if __name__ == '__main__':
    solve()
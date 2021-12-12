def solve():
    input = open('day1.txt', 'r')
    depthList = []
    for line in input:
        depthList.append(int(line))
    print(coutDepthIncreases(depthList))

SLIDE_WINDOW = 3
def coutDepthIncreases(depthList):
    count = 0
    for i in range(len(depthList) - SLIDE_WINDOW):
        count += 1 if((depthList[i + SLIDE_WINDOW] - depthList[i]) > 0) else 0
    return count

if __name__ == '__main__':
    solve()
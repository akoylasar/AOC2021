def solve():
    input = open('day2.txt', 'r')
    position = getSubmarineLocation(input.readlines())
    print(position[0] * position[1]) # horizontalPos * depth

def getSubmarineLocation(submarineRoute):
    x = 0
    y = 0
    for instruction in submarineRoute:
        i = instruction.split(' ') # each instruction has a direction and a step size e.g `forward 4`
        step = int(i[1]);
        if (i[0] == 'forward'):
            x += step
        elif (i[0] == 'down'):
            y += step
        else: # (i[0] == 'up')
            y -= step
    return x, y

if __name__ == '__main__':
    solve()
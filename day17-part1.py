import time
import re

def solve(xr, yr):
    # with the assumption that the target block is below zero
    # once the probe is back to zero we want to ensure that:
    # 1. we don't miss the target
    # 2. we want the biggest possible move in the y direction.
    # This is equivalent to the highest y value the probe can reach.
    # The only y velocity that satisfies these two conditions is absolute value of minimum of y range, minus 1.
    # So if the range say is -5 then the corresponding vy is 4 and consequently to calculate the highest y achieved:
    # (1 + 2 + 3 + 4) == 4 * 5 / 2 clearly a geometric sequence is calculated.
    vy = -min(yr) - 1
    maxH = (vy * (vy + 1)) // 2
    print(maxH)

if __name__ == '__main__':
    with open('day17.txt', 'r') as file:
        nput = [int(x) for x in re.findall(r'-*[1-9]+', file.readline())]
    xr = nput[:2]
    yr = nput[2:]
    start = time.time()
    solve(xr, yr)
    print("%s seconds" % (time.time() - start))
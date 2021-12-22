import math
import time
import re

def solve(xr, yr):
    def calculateMaxHeight(v):
        xv, yv = v
        xp, yp = 0, 0 # previous x and y
        maxY = yp
        n = 1
        while True:
            y = yp + yv
            x = xp + xv
            maxY = max(y, maxY)
            if xr[0] <= x <= xr[1] and yr[0] <= y <= yr[1]: # hit
                # print("hit with " + str(v[0]) + ", " + str(v[1]) + " with max height " + str(maxY))
                return maxY, True
            if xp <= xr[1] <= x or y <= yr[0] <= yp: # miss
                return maxY, False
            xp = x
            yp = y
            xv += 0 if xv == 0 else 1 if xv < 0 else -1
            yv -= 1
            n += 1
    # with the assumption that the target block is below zero
    hits = []
    r = -min(yr)
    xmin = round((math.sqrt(8 * xr[0] + 1) - 1) / 2)
    # Values less than xmin never make it to the target area because the vx reaches zero before
    # the probe is at low range of x-axis (xr[0).
    # The formula is re-arrangement of n * (n + 1) / 2 = x to solve for n where x is the low range of x-axis.
    # Values above the high range of x-axis (xr[1]) on the other hand would cause an overshoot
    # right after the first step of moving in the x direction.
    for vx in range(xmin, xr[1] + 1):
        for vy in range(-r, r): # TODO: fix ugly hardcoded hack
            v = vx, vy
            h, hit = calculateMaxHeight(v)
            if hit:
                hits.append(v)
    print(len(hits))

if __name__ == '__main__':
    with open('day17.txt', 'r') as file:
        nput = [int(x) for x in re.findall(r'-*[1-9]+', file.readline())]
    xr = nput[:2]
    yr = nput[2:]
    start = time.time()
    solve(xr, yr)
    print("%s seconds" % (time.time() - start))
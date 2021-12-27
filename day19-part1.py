import time

# trasnforms from xyz (right-up-forward) to other configs (all in left-handed):
pxpypz = lambda x, y, z: (x,   y,  z)
pxpzny = lambda x, y, z: (x,   z, -y)
pxnynz = lambda x, y, z: (x,  -y, -z)
pxnzpy = lambda x, y, z: (x,  -z,  y)
nxnypz = lambda x, y, z: (-x, -y,  z)
nxpzpy = lambda x, y, z: (-x,  z,  y)
nxpynz = lambda x, y, z: (-x,  y, -z)
nxnzny = lambda x, y, z: (-x, -z, -y)

pynxpz = lambda x, y, z: (y,  -x,  z)
pypzpx = lambda x, y, z: (y,   z,  x)
pypxnz = lambda x, y, z: (y,   x, -z)
pynznx = lambda x, y, z: (y,  -z, -x)
nypxpz = lambda x, y, z: (-y,  x,  z)
nypznx = lambda x, y, z: (-y,  z, -x)
nynxnz = lambda x, y, z: (-y, -x, -z)
nynzpx = lambda x, y, z: (-y, -z,  x)

pzpynx = lambda x, y, z: (z,   y, -x)
pznxny = lambda x, y, z: (z,  -x, -y)
pznypx = lambda x, y, z: (z,  -y,  x)
pzpxny = lambda x, y, z: (z,   x,  y)
nzpypx = lambda x, y, z: (-z,  y,  x)
nzpxny = lambda x, y, z: (-z,  x, -y)
nznynx = lambda x, y, z: (-z, -y, -x)
nznxpy = lambda x, y, z: (-z, -x,  y)
rotations = [pxpypz, pxpzny, pxnynz, pxnzpy, nxnypz, nxpzpy, nxpynz, nxnzny,
             pynxpz, pypzpx, pypxnz, pynznx, nypxpz, nypznx, nynxnz, nynzpx,
             pzpynx, pznxny, pznypx, pzpxny, nzpypx, nzpxny, nznynx, nznxpy]

def areOverlapping(s0, s1): # s0 is set
    # s0's beacons are assumed to be with respect to global 0, 0, 0
    rotatedS1s = [[rotate(x, y, z) for x, y, z in s1] for rotate in rotations]
    for rs1 in rotatedS1s:
        for b1 in rs1:
            for b0 in s0:
                # b0 - b1 is translation
                transformed = set(map(lambda p: (p[0] + b0[0] - b1[0],
                                                 p[1] + b0[1] - b1[1],
                                                 p[2] + b0[2] - b1[2]), rs1))
                if len(s0.intersection(transformed)) >= 12:
                    return True, transformed
    return False, None

def solve(nput):
    # TODO: optimise this loop
    scannersToCheck = [nput[0]]
    transformedScanners = [set(nput[0])]
    beacons = set(nput[0])
    while scannersToCheck:
        toRemove = scannersToCheck.pop()
        sa = transformedScanners.pop()
        for sb in nput:
            if sb == toRemove:
                continue
            overlaps, transformed = areOverlapping(sa, sb)
            if overlaps and sb not in scannersToCheck:
                scannersToCheck.append(sb)
                transformedScanners.append(transformed)
                beacons = beacons.union(transformed)
        nput.remove(toRemove)
    print(len(beacons))

if __name__ == '__main__':
    with open('day19.txt', 'r') as file:
        lines = [l.strip() for l in file.readlines()]
        nput = [[]]
        for l in lines:
            if not l:
                nput.append([])
                continue
            if l[1] != '-':
                nput[-1].append(tuple((int(s) for s in l.split(','))))
    start = time.time()
    solve(nput)
    print("%s seconds" % (time.time() - start))

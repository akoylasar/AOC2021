import time
import numpy as np

def solve(lines):
    nput = np.array([l.split('|')[1].strip().split() for l in lines])
    nput = [x for l in nput for x in l if (len(x) == 2 or
                                           len(x) == 4 or
                                           len(x) == 3 or
                                           len(x) == 7)]
    print (len(nput))
if __name__ == '__main__':
    with open('day8.txt', 'r') as file:
        lines = file.readlines()
    start = time.time()
    solve(lines)
    print("%s seconds" % (time.time() - start))
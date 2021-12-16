import time
import re
from collections import defaultdict

def solve(template, rules, iters = 40):
    pairCounter = defaultdict(lambda : 0)
    for i in range(len(template) - 1):
        l = template[i]
        r = template[i + 1]
        pairCounter[l + r] += 1
    charCounter = defaultdict(lambda: 0)
    for i in range(iters):
        newCounter = defaultdict(lambda : 0)
        for pair in pairCounter:
            step = pairCounter[pair]
            val = rules[pair]
            charCounter[val] += step
            l = pair[0] + val
            r = val + pair[1]
            newCounter[l] += step
            newCounter[r] += step
        pairCounter = newCounter
    for p in template:
        charCounter[p] += 1
    counts = list(charCounter.values())
    counts.sort()
    print(counts[-1] - counts[0])

if __name__ == '__main__':
    with open('day14.txt', 'r') as file:
        lines = file.readlines()
    template = lines[0].strip().split()[0]
    instructions = {}
    for line in lines[2:]:
        c = re.split(r'\W+', line.strip())
        instructions[c[0]] = c[1]
    start = time.time()
    solve(template, instructions)
    print("%s seconds" % (time.time() - start))
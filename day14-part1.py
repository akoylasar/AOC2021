import time
from collections import Counter
import re

def solve(template, rules):
    i = 0
    while i < 10:
        polymer = []
        for j in range(len(template) - 1):
            polymer.append(template[j])
            key = template[j] + template[j + 1]
            polymer.append(rules[key])
        polymer.append(template[-1])
        template = polymer
        i += 1
    s = Counter(template).most_common()
    print(s[0][1] - s[-1][1])

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
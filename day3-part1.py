import numpy as np
from collections import Counter

def solve():
    with open('day3.txt', 'r') as file:
        lines = file.readlines()
    input = np.array([[int(s) for s in line.strip("\n")] for line in lines])
    print(getSubmarinePowerConsumption(input))

def getSubmarinePowerConsumption(input):
    g = [Counter(input[0:, i]).most_common(1)[0][0] for i in range(len(input[0]))]
    e = [1 - x for x in g]
    gamma = sum([g[len(g) - i - 1] * (1 << i) for i in range(len(g))])
    epsilon = sum([e[len(e) - i - 1] * (1 << i) for i in range(len(e))])
    return gamma * epsilon

if __name__ == '__main__':
    solve()
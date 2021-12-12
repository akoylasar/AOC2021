import time

def solve(lines):
    # pad edges with zeros
    w = len(lines[0].strip("\n"))
    h = len(lines)
    inf = 10
    hmap = [[inf] * (w + 2)]
    for line in lines:
        row = [inf]
        row.extend(int(n) for n in line.strip("\n"))
        row.append(inf)
        hmap.append(row)
    hmap.append([inf] * (w + 2))
    convOp = lambda x, a, b, c, d: int(x < a) + int(x < b) + int(x < c) + int(x < d)
    lowPoints = [(hmap[i][j] + 1) * int(convOp(hmap[i][j],
                                               hmap[i - 1][j],
                                               hmap[i + 1][j],
                                               hmap[i][j - 1],
                                               hmap[i][j + 1]) == 4) for j in range(1, w + 1) for i in range(1, h + 1)]
    print(sum(lowPoints))

# def solve(lines):
#     # pad edges with zeros
#     w = len(lines[0].strip("\n"))
#     h = len(lines)
#     inf = 10
#     hmap = [[inf] * (w + 2)]
#     for line in lines:
#         row = [inf]
#         row.extend(int(n) for n in line.strip("\n"))
#         row.append(inf)
#         hmap.append(row)
#     hmap.append([inf] * (w + 2))
#     convOp = lambda x, a, b, c, d: int(x < a) + int(x < b) + int(x < c) + int(x < d)
#     risk = []
#     i = 1
#     while i < h + 1:
#         j = 1
#         while j < w + 1:
#             if (convOp(hmap[i][j],
#                        hmap[i - 1][j],
#                        hmap[i + 1][j],
#                        hmap[i][j - 1],
#                        hmap[i][j + 1]) == 4):
#                 risk.append(hmap[i][j] + 1)
#                 j += 2
#                 continue
#             j += 1
#         i += 1
#     print(sum(risk))

if __name__ == '__main__':
    with open('day9.txt', 'r') as file:
        lines = file.readlines()
    start = time.time()
    solve(lines)
    print("%s seconds" % (time.time() - start))
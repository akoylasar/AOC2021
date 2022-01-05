import time
import numpy as np

def solve(algoStr, image):
    def getValue(j, i, inputImg):
        tl = inputImg[j-1][i-1] * 256
        t =  inputImg[j-1][i] * 128
        tr = inputImg[j-1][i+1] * 64
        l =  inputImg[j][i-1] * 32
        c =  inputImg[j][i] * 16
        r =  inputImg[j][i+1] * 8
        bl = inputImg[j+1][i-1] * 4
        b =  inputImg[j+1][i] * 2
        br = inputImg[j+1][i+1]
        index = int(tl + t + tr + l + c + r + bl + b + br)
        return int(algoStr[index] == '#')
    def display(image):
        for r in image:
            for x in r:
                print('#' if x else '.', end='')
            print()
        print()
    i = 0
    outputImg = image
    first = algoStr[0] == '#'
    last = algoStr[-1] == '#'
    while i < 2:
        padValue = 0 if i == 0 else first if (i % 2) else last
        h, w = outputImg.shape
        inputImg = np.pad(outputImg, ((2, 2),), 'constant', constant_values=(padValue, padValue))
        outputImg = np.array([[getValue(j + 1, k + 1, inputImg) for k in range(0, w + 2)] for j in range(0, h + 2)])
        i += 1
    display(outputImg)
    print(sum(sum(outputImg)))

if __name__ == '__main__':
    with open('day20.txt', 'r') as file:
        lines = file.readlines()
        algoStr = lines[0].strip()
        image = np.array([[int(x == '#') for x in l.strip()] for l in lines[2:]])
    start = time.time()
    solve(algoStr, image)
    print("%s seconds" % (time.time() - start))
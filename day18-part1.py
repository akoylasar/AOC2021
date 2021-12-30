import time
import queue

class Node:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right
    def __str__(self):
        return '[' + str(self.left) + ',' + str(self.right) + ']'

def parseBinaryTree(line):
    i = 1
    stack = [Node()]
    while i < len(line) - 1:
        if line[i] == '[':
            newNode = Node()
            stack[-1].left = newNode
            stack.append(newNode)
        elif line[i].isdigit():
            stack[-1].left = int(line[i])
        elif line[i] == ',':
            i += 1
            if line[i].isdigit():
                stack[-1].right = int(line[i])
            else:  # after a ',' we expect a '[' or a digit only, this else cover the '[' case
                newNode = Node()
                stack[-1].right = newNode
                stack.append(newNode)
        elif line[i] == ']':
            stack.pop()
        i += 1
    return stack.pop()

def reduce(tree):
    return Node()

def magnitude(tree):
    return 0

def solve(trees):
    result = trees[0]
    i = 1
    while i < len(trees):
        result = reduce(Node(result, trees[i]))
        i += 1
    print(magnitude(result))

if __name__ == '__main__':
    with open('day18.txt', 'r') as file:
        lines = [l.strip() for l in file.readlines()]
    trees = [parseBinaryTree(line) for line in lines]
    start = time.time()
    solve(trees)
    print("%s seconds" % (time.time() - start))

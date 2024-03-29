import math
import time

class Node:
    def __init__(self, parent=None, left=None, right=None, data=None):
        self.parent = parent
        self.left = left
        self.right = right
        self.data = data
    def __str__(self):
        if self.data is not None:
            return str(self.data)
        return '[' + str(self.left) + ',' + str(self.right) + ']'

def parseBinaryTree(line):
    i = 1
    stack = [Node()]
    while i < len(line):
        if line[i] == '[':
            newNode = Node(stack[-1])
            stack[-1].left = newNode
            stack.append(newNode)
        elif line[i].isdigit():
            newNode = Node(stack[-1], None, None, int(line[i]))
            stack[-1].left = newNode
        elif line[i] == ',':
            i += 1
            if line[i].isdigit():
                newNode = Node(stack[-1], None, None, int(line[i]))
                stack[-1].right = newNode
            else:  # after a ',' we expect a '[' or a digit only, this else cover the '[' case
                newNode = Node(stack[-1])
                stack[-1].right = newNode
                stack.append(newNode)
        elif line[i] == ']':
            if len(stack) == 1:
                break
            stack.pop()
        i += 1
    return stack.pop()

def addToLeftNeighbour(node):
    value = node.left.data
    if value == 0: return
    while node.parent and node == node.parent.left:
        node = node.parent
    if node.parent:
        neighbour = node.parent.left
        while neighbour.data is None:
            neighbour = neighbour.right
        neighbour.data += value

def addToRightNeighbour(node):
    value = node.right.data
    if value == 0: return
    while node.parent and node == node.parent.right:
        node = node.parent
    if node.parent:
        neighbour = node.parent.right
        while neighbour.data is None:
            neighbour = neighbour.left
        neighbour.data += value

def split(number: Node):
    if number.data is not None:
        if number.data >= 10:
            c = number.data / 2
            number.data = None
            leftNode = Node(number, None, None, int(c))
            rightNode = Node(number, None, None, int(math.ceil(c)))
            number.left = leftNode
            number.right = rightNode
            return True
        else: return False
    ls = split(number.left)
    if ls: return True
    rs = split(number.right)
    if rs: return True
    return False

def explode(number: Node):
    n = getExplodingNumber(number, 0)
    if n is None: return False
    addToLeftNeighbour(n)
    addToRightNeighbour(n)
    n.left = None
    n.right = None
    n.data = 0
    return True

def getExplodingNumber(number: Node, i=0):
    if i == 4 and number.data is None:
        return number
    if number.left is not None:
        el = getExplodingNumber(number.left, i+1)
        if el is not None: return el
    if number.right is not None:
        er = getExplodingNumber(number.right, i+1)
        if er is not None: return er
    return None

def reduce(number: Node):
    return explode(number) or split(number)

def addNumbers(left:Node, right:Node):
    parent = Node(None, left, right)
    left.parent = parent
    right.parent = parent
    return parent

def getMagnitude(number: Node):
    if number.data is None:
        return 3 * getMagnitude(number.left) + 2 * getMagnitude(number.right)
    return number.data

def solve(numbers):
    number = numbers[0]
    for other in numbers[1:]:
        number = addNumbers(number, other)
        while reduce(number):
            continue
    print(getMagnitude(number))

if __name__ == '__main__':
    with open('day18.txt', 'r') as file:
        numbers = [parseBinaryTree(l.strip()) for l in file.readlines()]
    start = time.time()
    solve(numbers)
    print("%s seconds" % (time.time() - start))

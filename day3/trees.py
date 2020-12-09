import numpy as np

trees = []
with open("day3/input.txt", "r") as fp:
    for line in fp:
        trees.append([char for char in line if char != "\n"])

#part 1
down = 0
right = 0
treeCount = 0

while down < len(trees):
    if(right >= len(trees[down])):
        right = right-len(trees[down])
    if(trees[down][right] == "#"):
        treeCount += 1
    down += 1
    right += 3

print(treeCount)

#part 2


downArr = [1, 1, 1, 1, 2]
rightArr = [1, 3, 5, 7, 1]
ctr = 0
treeCountAll = []

while ctr < len(downArr):
    down = 0
    right = 0
    treeCount = 0
    while down < len(trees):
        if(right >= len(trees[down])):
            right = right-len(trees[down])
        if(trees[down][right] == "#"):
            treeCount += 1
        down += downArr[ctr]
        right += rightArr[ctr]
    treeCountAll.append(treeCount)
    ctr += 1

print(treeCountAll)
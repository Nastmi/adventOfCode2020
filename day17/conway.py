from time import time

startInput = open("day17/input.txt").read().split("\n")
print(startInput)
#part 1


def get_neighbors(cube):
    x, y, z = cube
    neighbors = {(x1, y1, z1) for x1 in range(x-1,x+2) for y1 in range(y-1,y+2) for z1 in range(z-1,z+2)}
    neighbors.remove((x,y,z))
    return neighbors

actives = set()
for i, __ in enumerate(startInput):
    for j, __ in enumerate(startInput[i]):
        if(startInput[i][j] == "#"):
            actives.add((j, i, 0))

for i in range(6):
    new_actives = set()
    for cube in actives:
        neighbors = get_neighbors(cube)
        intersection = neighbors & actives
        if(len(intersection) == 2 or len(intersection) == 3):
            new_actives.add(cube)
        for cube1 in neighbors:
            neighbors1 = get_neighbors(cube1)
            intersection1 = neighbors1 & actives
            if(len(intersection1) == 3 """and cube1 not in actives"""):
                new_actives.add(cube1)
    actives = new_actives.copy()

print(len(actives))

#part 2

def get_neighbors(cube):
    x, y, z, w = cube
    neighbors = {(x1, y1, z1, w1) for x1 in range(x-1,x+2) for y1 in range(y-1,y+2) for z1 in range(z-1,z+2) for w1 in range(w-1, w+2)}
    neighbors.remove((x,y,z,w))
    return neighbors

actives = set()
for i, __ in enumerate(startInput):
    for j, __ in enumerate(startInput[i]):
        if(startInput[i][j] == "#"):
            actives.add((j, i, 0, 0))

sTime = time()
for i in range(6):
    new_actives = set()
    for cube in actives:
        neighbors = get_neighbors(cube)
        intersection = neighbors & actives
        if(len(intersection) == 2 or len(intersection) == 3):
            new_actives.add(cube)
        for cube1 in neighbors:
            neighbors1 = get_neighbors(cube1)
            intersection1 = neighbors1 & actives
            if(len(intersection1) == 3 """and cube1 not in actives"""):
                new_actives.add(cube1)
    actives = new_actives.copy()

print(len(actives), time() - sTime)
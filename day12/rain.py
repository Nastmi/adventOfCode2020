instruction_set = [(item[0], int(item[1:])) for item in open("day12/input.txt").read().split("\n")]

#part 1
directions = {"E":(1, "x"), "N":(1, "y"), "W":(-1, "x"), "S":(-1, "y")}
turn = ("E", "N", "W", "S")
coords = {"x":0, "y":0}
direction = "E"
for ins, value in instruction_set:
    if ins in directions:
        coords[directions[ins][1]] += value * directions[ins][0]
    elif ins == "F":
        coords[directions[direction][1]] += value * directions[direction][0]
    else:
        mv = (int(value/90) if ins == "L" else int(-value/90)) + turn.index(direction)
        mv = (mv - len(turn)) if mv >= len(turn) else mv
        direction = turn[mv]
print(abs(coords["x"]) + abs(coords["y"]))

#part 2
coords = {"x":10, "y":1}
ship_coords = {"x":0, "y":0}
direction = "E"
for ins, value in instruction_set:
    if ins in directions:
        coords[directions[ins][1]] += value * directions[ins][0]
    elif ins == "F":
        ship_coords["x"] += value*coords["x"]
        ship_coords["y"] += value*coords["y"]
    else:
        mv = (int(value/90) if ins == "L" else int(-value/90)) + turn.index(direction)
        mv = (mv - len(turn)) if mv >= len(turn) else mv
        mv2 = mv + 1
        mv2 = (mv2 - len(turn)) if mv2 >= len(turn) else mv2
        dir1 = turn[mv2]
        dir2 = turn[mv]
        coords[directions[dir1][1]], coords[directions[dir2][1]]= coords["y"]*directions[dir1][0], coords["x"]*directions[dir2][0]
print(abs(ship_coords["x"]) + abs(ship_coords["y"]))
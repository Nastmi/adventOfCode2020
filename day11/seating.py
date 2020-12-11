seats = open("day11/input.txt").read().split("\n")

#part 1
def adjacent(x, y):
    adj = []
    if(x > 0 and y > 0):
        adj.append(seats[y-1][x-1])  
    if(x > 0):
        adj.append(seats[y][x-1]) 
    if(x < len(seats[y])-1 and y > 0):
        adj.append(seats[y-1][x+1])
    if(x < len(seats[y])-1):
        adj.append(seats[y][x+1])
    if(x < len(seats[y])-1 and y < len(seats)-1):
        adj.append(seats[y+1][x+1])
    if(y < len(seats)-1):
        adj.append(seats[y+1][x])
    if(x > 0 and y < len(seats)-1):
        adj.append(seats[y+1][x-1])
    if(y > 0):
        adj.append(seats[y-1][x])
    return adj



def simulate_seats(seats, t):
    new_seats = []
    for y, ln in enumerate(seats):
        cur_line = ""
        for x, seat in enumerate(seats[y]):
            adj = adjacent(x, y)
            if seat == ".":
                cur_line += "."
            else:
                if(seat == "L" and adj.count("#") == 0):
                    cur_line += "#"
                elif(seat == "#" and adj.count("#") >= t):
                    cur_line += "L"
                else:
                    cur_line += seat
        new_seats.append(cur_line) 
    return new_seats

"""while True:
    new_seats = simulate_seats(seats, 4)
    if(new_seats == seats):
        print(sum([item.count("#") for item in new_seats]))
        break
    seats = new_seats.copy()"""

#part 2

def adjacent(x, y):
    adj = []
    oX = x
    oY = y
    while x > 0 and y > 0:
        x -= 1
        y -= 1
        if(seats[y][x] == "#" or seats[y][x] == "L"):
            adj.append(seats[y][x])  
            break
    x = oX
    y = oY
    while x > 0:
        x -= 1
        if(seats[y][x] == "#" or seats[y][x] == "L"):
            adj.append(seats[y][x])
            break  
    x = oX
    y = oY
    while x < len(seats[y])-1 and y > 0:
        x += 1
        y -= 1
        if(seats[y][x] == "#" or seats[y][x] == "L"):
            adj.append(seats[y][x]) 
            break 
    x = oX
    y = oY
    while x < len(seats[y])-1:
        x += 1
        if(seats[y][x] == "#" or seats[y][x] == "L"):
            adj.append(seats[y][x])  
            break
    x = oX
    y = oY
    while x < len(seats[y])-1 and y < len(seats)-1:
        x += 1
        y += 1
        if(seats[y][x] == "#" or seats[y][x] == "L"):
            adj.append(seats[y][x])  
            break
    x = oX
    y = oY
    while y < len(seats)-1:
        y += 1
        if(seats[y][x] == "#" or seats[y][x] == "L"):
            adj.append(seats[y][x]) 
            break
    x = oX
    y = oY
    while x > 0 and y < len(seats)-1:
        x -= 1
        y += 1
        if(seats[y][x] == "#" or seats[y][x] == "L"):
            adj.append(seats[y][x])  
            break
    x = oX
    y = oY
    while y > 0:
        y -= 1
        if(seats[y][x] == "#" or seats[y][x] == "L"):
            adj.append(seats[y][x])  
            break
    return adj

while True:
    new_seats = simulate_seats(seats, 5)
    if(new_seats == seats):
        print(sum([item.count("#") for item in new_seats]))
        break
    seats = new_seats.copy()

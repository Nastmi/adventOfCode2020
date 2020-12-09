passports = list(map(str.strip, open("day5/input.txt")))

#part 1

ids = []
for passport in passports:
    rows = passport[:7]
    columns = passport[7:]
    upr = 127
    lwr = 0
    row = 0
    testRow = "FBFBBFF"
    #f lower b upper
    for r in rows:
        if(r == "F"):
            upr = int((upr+lwr)/2)
            row = lwr
        elif(r == "B"):
            lwr = round((upr+lwr)/2)
            row = upr
    upr = 7
    lwr = 0
    col = 0
    testCol = "RLR"
    for c in columns:
        if(c == "L"):
            upr = int((upr+lwr)/2)
            col = lwr
        elif(c == "R"):
            lwr = round((upr+lwr)/2)
            col = upr
    ids.append(row*8+col)
print(max(ids))

#part 2


for cId in ids:
    if((cId+2) in ids and (cId+1) not in ids):
        print(cId+1)
import numpy as np
from math import ceil
l = open("day13/input.txt").read().split("\n")
time = int(l[0])
busses = [int(n) for n in l[1].split(",") if n != "x"]
#part 1
for bus in busses:
    print(bus - time % bus, bus)

#original solution
"""for bus in busses:
    print(ceil(time/bus)*bus%time, bus, (ceil(time/bus)*bus-time)*bus)"""


#part 2. Took long because maths :(
busses = [(i, int(n)) for i, n in enumerate(l[1].split(",")) if n != "x"]
remainders = [-item[0] for item in busses]
prod = 1
for i, t in busses:
    prod *= t
prodList = [prod//item[1] for item in busses]
inverses = [pow(prodList[i] ,-1, item[1]) for i, item in enumerate(busses)]
finals = [prod1*remainder*inverse for prod1, remainder, inverse in zip(prodList, remainders, inverses)]
print(sum(finals) % prod)






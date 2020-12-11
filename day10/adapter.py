from functools import lru_cache
adapters = [0]
adapters.extend([int(item) for item in open("day10/input.txt").read().split("\n")])
adapters.append(max(adapters)+3)
#part 1
adapters.sort()
count = {1:0, 2:0, 3:0}
ctr = 1
while ctr < len(adapters):
    count[adapters[ctr]-adapters[ctr-1]] += 1
    ctr += 1
print(count[1] * count[3]-1)


#part 2
def follows(num):
    followSet = set()
    followSet.add(num + 1) if num+1 in adapters else followSet.update(set())
    followSet.add(num + 2) if num+2 in adapters else followSet.update(set())
    followSet.add(num + 3) if num+3 in adapters else followSet.update(set())
    return followSet

@lru_cache(3)
def count_valids(num):
    cur_follow = follows(num)
    total = 0
    if(len(cur_follow) == 0):
        return 1
    for num1 in cur_follow:
        total += count_valids(num1)
    return total


print(count_valids(0))

#Old solution, before lru_cache. Seperates the list of adapters into mutliple smaller lists, where n-(n-1) = 3. 

"""def follows(num, adap):
    followSet = set()
    followSet.add(num + 1) if num+1 in adap else followSet.update(set())
    followSet.add(num + 2) if num+2 in adap else followSet.update(set())
    followSet.add(num + 3) if num+3 in adap else followSet.update(set())
    return followSet"""

"""sep = []
seqStart = 0
for i in range(1, len(adapters)):
    if (adapters[i] - adapters[i-1]) == 3 or (adapters[i-1] - adapters[i]) == 3:
        sep.append(adapters[seqStart:i])
        seqStart = i

print(sep)    
for item in sep:
    total = total*count_valids(item[0], item)
    print(count_valids(item[0], item))
print(total)"""








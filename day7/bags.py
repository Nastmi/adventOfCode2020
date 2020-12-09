import sys
f = open("day7/input.txt").read()
rules = f.split("\n")
bags = {}
for rule in rules:
    rule.strip(".")
    sep = rule.split(" contain ")
    bag = sep[0].rstrip("s")
    others = sep[1].split(", ")
    if(not others[0].startswith("no")):
        bags[bag] = {(int(item[0]), "".join(item[2:]).rstrip(".").rstrip("s")) for item in others}

#part 1
def parents(bag):
    parents = set()
    for key in bags.keys():
        for value in bags[key]:
            check_bag = value[1]
            if(check_bag == bag):
                parents.add(key)
    return parents

def all_parents(bag):
    cur_parents = parents(bag)
    if len(cur_parents) == 0:
        return set()
    for b in cur_parents:
        cur_parents = cur_parents | all_parents(b)
    return cur_parents

print(len(all_parents("shiny gold bag")))

#part 2

def children(bag):
    return list(bags[bag]) if bag in bags.keys() else []

def all_children(bag):
    cur_children = children(bag)
    total = 1
    if bag not in bags.keys():
        return 1
    for count, b in cur_children:
        total += count * all_children(b)
    return total

print(all_children("shiny gold bag")-1)



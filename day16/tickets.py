import numpy as np

l = open("day16/input.txt").read().split("\n\n")
first = l[0].split("\n")
rules = {}
for line in first:
    s1 = line.split(": ")
    name = s1[0]
    s2 = s1[1].split(" or ")
    range1 = s2[0].split("-")
    range2 = s2[1].split("-")
    rules[name] = [(range1[0],range1[1]),(range2[0],range2[1])]
per_ticket = l[1].split("\n")[1].split(",")
all_tickets = l[2].split("\n")[1:]
#part 1
invalids = []
for ticket in all_tickets:
    sep = ticket.split(",")
    for data in sep:
        data = int(data)
        is_valid = False
        for rng1,rng2 in rules.values():
            if(int(rng1[0]) <= data <= int(rng1[1]) or int(rng2[0]) <= data <= int(rng2[1])):
                is_valid = True
                break
        if not is_valid:
            invalids.append(int(data))
            
print(len(invalids))

#part 2
invalids = []
for ticket in all_tickets:
    sep = ticket.split(",")
    for data in sep:
        data = int(data)
        is_valid = False
        for rng1,rng2 in rules.values():
            if(int(rng1[0]) < data < int(rng1[1]) or int(rng2[0]) < data < int(rng2[1])):
                is_valid = True
                break
        if not is_valid:
            invalids.append(ticket)
valids = all_tickets.copy()
for ticket in all_tickets:
    for ticket2 in invalids:
        if ticket == ticket2:
            valids.remove(ticket2)
            break
all_rules = []

for ticket in valids:
    sep = ticket.split(",")
    rules_for_ticket = []
    for data in sep:
        rules_for_data = []
        data = int(data)
        for key, item in rules.items():
            rng1, rng2 = item
            if(int(rng1[0]) <= data <= int(rng1[1]) or int(rng2[0]) <= data <= int(rng2[1])):
                rules_for_data.append(key)
        rules_for_ticket.append(rules_for_data)
    all_rules.append(rules_for_ticket)

data_to_compare = all_rules[0]
end_rules = []
for i in range(len(all_rules[0])):
    inter = set(data_to_compare[i])
    for j in range(len(all_rules)):
        comp = set(all_rules[j][i])
        inter = inter.intersection(comp)
    end_rules.append(inter)

final_rules = end_rules.copy()
for i in range(21):
    for j, item in enumerate(end_rules):
        if len(item) == i:
            for k, item in enumerate(end_rules):
                if(k != j):
                    final_rules[k] = final_rules[k] - final_rules[j]

final_rules = [list(item) for item in final_rules]
print(final_rules)

dep_rules = []
for i, rule in enumerate(final_rules):
    if(rule[0].startswith("departure")):
        dep_rules.append(int(per_ticket[i]))
prod = 1
for item in dep_rules:
    prod*=item
print(prod)



    



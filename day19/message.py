l = open("day19/input2.txt").read().split("\n\n")
rules_un = l[0].split("\n")
messages = l[1].split("\n")
rules = {}
for rule in rules_un:
    sep = rule.split()
    num = sep[0][:-1]
    rl = " ".join(sep[1:]).split(" | ")
    rules[num] = rl




def get_rules(num):
    if(num == "a" or num == "b"):
        return num
    cur_rules = rules[num][0].split()
    correct = ""
    for rule in cur_rules:
        correct += get_rules(rule)
    correct += " "
    if(len(rules[num]) == 2):
        cur_rules2 = rules[num][1].split()
        for rule2 in cur_rules2:
            correct += get_rules(rule2)
    correct + " "
    return correct

print(get_rules("0"))

    
#for message in messages:

 

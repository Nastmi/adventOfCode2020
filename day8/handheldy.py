f = open("day8/input.txt").read().split("\n")
table = [[item.split()[0],int(item.split()[1])] for item in f]

def runSet(tableToRun):
    innerInstructions = []
    innerCtr = 0
    innerAcc = 0
    while innerCtr not in innerInstructions:
        if(innerCtr == len(tableToRun)):
            return {"acc":innerAcc, "run": True}
        innerInstructions.append(innerCtr)
        instruction, value = tableToRun[innerCtr]
        if(instruction == "acc"):
            innerCtr += 1
            innerAcc += value
        elif(instruction == "jmp"):
            innerCtr +=  value
        else:
            innerCtr += 1
    return {"acc":innerAcc, "run": False, "instructions": innerInstructions}


#part 1
print(runSet(table)["acc"])
#part 2
instructions = runSet(table)["instructions"]
while True:
    fixedTable = []
    fixedTable.extend([item.copy() for item in table])
    place = instructions[-1]
    value = table[place][0]
    if value == "jmp":
        fixedTable[place][0] = "nop"
    elif value == "nop":
        fixedTable[place][0] = "jmp"
    else:
        instructions.pop()
        continue
    curSet = runSet(fixedTable)
    if(curSet["run"] == True):
        print(curSet["acc"])
        break
    instructions.pop()
    
    
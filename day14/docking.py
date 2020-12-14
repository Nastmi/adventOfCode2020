inf = open("day14/input.txt").read().split("\n")

#part 1
def apply_mask(num, mask):
    num = bin(num)[2:]
    num = num.zfill(len(mask))
    new_num = ""
    for i, bit in enumerate(num):
        if(mask[i] == "X"):
            new_num = new_num + bit
            continue
        new_num = new_num + "1" if mask[i] == "1" else  new_num +"0"
    return new_num

memory = dict()
mask = ""
for line in inf:
    ln = line.split(" ")
    if(ln[0] == "mask"):
        mask = ln[2]
    else:
        mem_loc = ln[0][4:-1]
        num = apply_mask(int(ln[2]), mask)
        memory[mem_loc] = int(num, 2)
print(sum([num for num in memory.values()]))

#part 2
def apply_floating_mask(num, mask):
    num = bin(num)[2:]
    num = num.zfill(len(mask))
    new_num = ""
    for i, bit in enumerate(num):
        if(mask[i] == "X"):
            new_num = new_num + "X"
            continue
        new_num = new_num + "1" if mask[i] == "1" else  new_num + bit
    return new_num

def get_all_combos(num):
    combos = []
    for i in range(2**num.count("X")):
        new_num = ""
        num_to_apply = bin(i)[2:]
        num_to_apply = [b for b in num_to_apply.zfill(num.count("X"))]
        for bit in num:
            if(bit == "X"):
                new_num += num_to_apply[0]
                num_to_apply.pop(0)
            else:
                new_num += bit
        combos.append(new_num)
    return combos

memory = dict()
mask = ""
for line in inf:
    ln = line.split(" ")
    if(ln[0] == "mask"):
        mask = ln[2]
    else:
        mem_loc_m = apply_floating_mask(int(ln[0][4:-1]), mask)
        num = int(ln[2])
        loc = get_all_combos(mem_loc_m)
        for mem_loc in loc:
            memory[int(mem_loc, 2)] = num


print(sum([num for num in memory.values()]))
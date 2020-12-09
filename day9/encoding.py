numbers = open("day9/input.txt").read().split("\n")
numbers = [int(num) for num in numbers]
pos = 0
seq = numbers[:25]
cur_num = numbers[25]
w_num = 0
while True:
    seq = numbers[pos:25+pos]
    cur_num = numbers[25+pos]
    is_correct = False
    for num in seq:
        if((cur_num-num) in seq):
            is_correct = True
            break
    if(not is_correct):
        print(cur_num)
        w_num = cur_num
        break
    pos += 1

r_seq = [] 
ctr = 0 
while True:
    seq = []
    inner_ctr = ctr 
    while sum(seq) < w_num:
        seq.append(numbers[inner_ctr])
        if(sum(seq) == w_num):
            r_seq = seq
            break
        inner_ctr += 1
    if(len(r_seq) > 0):
        break
    ctr += 1

print(max(r_seq)+min(r_seq))
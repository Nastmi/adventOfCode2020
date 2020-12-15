import time

nums = [2,1,10,11,0,6]

#part 1
while len(nums) < 2020:
    cur_num = nums[-1]
    if(nums.count(cur_num) > 1):
        nums.append(nums[:-1][::-1].index(cur_num)+1)
    else:
        nums.append(0)

print(len(nums), nums[-1])

#part 2

nums = [2,1,10,11,0,6]
indexes = {x:[nums.index(x)] for x in nums}
counts = {x:1 for x in nums}
ctr = len(nums)
t = time.time()
while ctr < 30000000:
    cur_num = nums[-1]
    if(counts[cur_num] > 1):
        new_num = indexes[cur_num][-1] - indexes[cur_num][-2]
        nums.append(new_num)
        if new_num in indexes.keys():
            indexes[new_num].append(ctr)
            counts[new_num] += 1
        else:
            indexes[new_num] = [ctr] 
            counts[new_num] = 1
    else:
        nums.append(0)
        indexes[0].append(ctr)
        counts[0] += 1
    ctr += 1
print(time.time()-t)
print(len(nums), nums[-1])
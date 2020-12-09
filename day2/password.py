passwords = list(map(str.strip, open("day2/input.txt")))
#part 1
valid = 0
for password in passwords:
    sep = password.split()
    ocur = sep[2].count(sep[1][:1])
    allowed = sep[0].split("-")
    if(int(allowed[1]) >= ocur >= int(allowed[0])):
        valid += 1
print(valid)

#part 2
valid = 0
for password in passwords:
    sep = password.split()
    curPass = sep[2]
    allowed = sep[0].split("-")
    low = int(allowed[0])-1
    high = int(allowed[1])-1
    if(((curPass[low] == sep[1][:1]) ^ (curPass[high] == sep[1][:1]))):
        valid += 1
print("other: ", valid)

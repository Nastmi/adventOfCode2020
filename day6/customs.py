f = open("day6/input.txt")
l = [item.split("\n") for item in f.read().split("\n\n")]

#part 1
total = 0
for group in l:
    answers = set()
    answers.update([char for ans in group for char in ans])
    total += len(answers)
print(total)

#part 2
total = 0
for group in l:
    answers = []
    for ans in group:
        answers.append({char for char in ans})
    inter = answers[0]
    for chars in answers:
        inter = inter.intersection(chars)
    total += len(inter)
print(total)
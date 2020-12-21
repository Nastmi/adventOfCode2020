from math import sqrt
l = open("day20/input.txt").read().split("\n\n")
images = {image.split("\n")[0][5:-1]:image.split("\n")[1:] for image in l}


#part 1
#solution 2801 * 3823 * 1759 * 2719 = 51214443014783
def get_all_conf(grid):
    all_configs = [grid, grid[::-1]]
    grid = ["".join(item) for item in list(zip(*grid[::-1]))]
    all_configs.extend([grid, grid[::-1]])
    grid = ["".join(item) for item in list(zip(*grid[::-1]))]
    all_configs.extend([grid, grid[::-1]])
    grid = ["".join(item) for item in list(zip(*grid[::-1]))]
    all_configs.extend([grid, grid[::-1]])
    return all_configs

def get_matches(grid1, grid2):
    borders1 = [grid1[0], "".join([item[-1] for item in grid1]), grid1[-1], "".join([item[0] for item in grid1])]
    borders2 = [grid2[-1], "".join([item[0] for item in grid2]), grid2[0], "".join([item[-1] for item in grid2])]
    for i, border1 in enumerate(borders1):
        if(border1 == borders2[i]):
            if(i == 0):
                return "top"
            elif(i == 1):
                return "right"
            elif(i == 2):
                return "bottom"
            elif(i == 3):
                return "left"
    return None


"""all_match = []
for key, image in images.items():
    for conf in get_all_conf(image):
        matches = []
        for key2, image2 in images.items():
            for conf2 in get_all_conf(image2):
                if(key != key2):
                    mtch = get_matches(conf, conf2)
                    if(mtch != None):
                        matches.append([mtch] + [key] + [key2])
        if(len(matches) == 2):
            all_match.append(matches)"""

#part 2
"""start = []
end = False
for key, image in images.items():
    for conf in get_all_conf(image):
        matches = []
        for key2, image2 in images.items():
            for conf2 in get_all_conf(image2):
                if(key != key2):
                    mtch = get_matches(conf, conf2)
                    if(mtch != None):
                        matches.append([mtch] + [key] + [key2] + [conf]) 
        if(len(matches) == 2):
            start.append(matches)
    if(end):
        break
for item in start:
    print(item)"""

"""grid = [["1951"]]
grid_conf = [[['#...##.#..', '..#.#..#.#', '.###....#.', '###.##.##.', '.###.#####', '.##.#....#', '#...######', '.....#..##', '#.####...#', '#.##...##.']]]
cur_conf = ['#...##.#..', '..#.#..#.#', '.###....#.', '###.##.##.', '.###.#####', '.##.#....#', '#...######', '.....#..##', '#.####...#', '#.##...##.']
start_config = ['#...##.#..', '..#.#..#.#', '.###....#.', '###.##.##.', '.###.#####', '.##.#....#', '#...######', '.....#..##', '#.####...#', '#.##...##.']
cur_key = "1951"""
grid = [["1759"]]
grid_conf = [[['..###...##', '#..##.#..#', '#......#..', '....#.....', '.#.#....##', '.......#..', '#.#......#', '##........', '#........#', '#.#.#..#..']]]
cur_conf = ['..###...##', '#..##.#..#', '#......#..', '....#.....', '.#.#....##', '.......#..', '#.#......#', '##........', '#........#', '#.#.#..#..']
start_config = ['..###...##', '#..##.#..#', '#......#..', '....#.....', '.#.#....##', '.......#..', '#.#......#', '##........', '#........#', '#.#.#..#..']
cur_key = "1759"


all_keys = [key for key in images.keys()]
for i in range(int(sqrt(len(images)))):
    for j in range(int(sqrt(len(images)))):
        for key, image in images.items():
            found_right = False
            for conf in get_all_conf(image):
                if(key != cur_key):
                    mtch = get_matches(cur_conf, conf)
                    if(mtch == "right"):
                        if(key in all_keys):
                            grid[i].append(key)
                            grid_conf[i].append(conf)
                            cur_conf = conf
                            all_keys.remove(key)
                            found_right = True
                            cur_key = key
                            break
    for key, image in images.items():
        found_bottom = False
        for conf in get_all_conf(image):
            if(key != cur_key):
                mtch = get_matches(start_config, conf)
                if(mtch == "bottom"):
                    grid.append([key])
                    grid_conf.append([conf])
                    start_config = conf
                    cur_conf = conf
                    found_bottom = True
                    cur_key = key
                    break
        if(found_bottom):
            break

"""for i in range(int(sqrt(len(images)))):
    for j in range(int(sqrt(len(images)))):
        for key, image in images.items():
            for conf in get_all_conf(image):
                if(key != cur_key):
                    mtch = get_matches(cur_conf, conf)
                    if(mtch == "right"):
                        if(key not in grid[i]):
                            grid[i].append(key)
                            grid_conf[i].append(conf)
                            cur_conf = conf
                            break
                        else:
                            if(j > 0):
                                j -= 1
    for key, image in images.items():
            for conf in get_all_conf(image):
                if(key != cur_key):
                    mtch = get_matches(start_config, conf)
                    if(mtch == "bottom"):
                        grid.append([key])
                        grid_conf.append([conf])
                        start_config = conf
                        cur_conf = conf
                        break"""

for i, item in enumerate(grid_conf):
    for j, image in enumerate(item):
        grid_conf[i][j].pop(0)
        grid_conf[i][j].pop(-1)
        for k, single in enumerate(image):
            new_s = single[1:-1]
            grid_conf[i][j][k] = new_s

indexes = [0, 6, 11, 12, 17, 18, 23, 24, 25, 31, 34, 37, 40, 43, 46]
monsters = 0
final_grid = []
for i, item in enumerate(grid_conf):
    for j in range(len(item[0])):
        ln = ""
        for k in range(len(item)):
            ln += item[k][j]
        final_grid.append(ln)

for conf in get_all_conf(final_grid):
    joined = "".join([line for item in conf for image in item for line in image])
    for i, __ in enumerate(joined):
        slc = joined[i:48+i]
        if(len(slc) < 48):
            break
        correct = 0
        for idx in indexes:
            if(slc[idx] == "#"):
                correct += 1
        if(correct == len(indexes)):
            monsters += 1
    print(monsters)

    
                








    


    
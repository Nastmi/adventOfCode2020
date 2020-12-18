expressions = open("day18/input.txt").read().split("\n")

finals = []


#part 1
def find_inner_par(expression):
    cur_pars = []
    for i, symbol in enumerate(expression):
            if(symbol == "("):
                cur_pars.append(i)
            elif(symbol == ")"):
                return (cur_pars[-1], i)

def solve_seq(expression):
    exp = expression.split()
    seq = []
    for symbol in exp:
        seq.append(symbol)
        if(len(seq) == 3):
            seq = [str(eval("".join(seq)))]
    return seq[0]  

finals = []
for expression in expressions:
    expression = "(" + expression + ")"
    while(not expression[:-1].isdigit() and expression[-1] == ")"):
        low, high = find_inner_par(expression)
        cur_exp = expression[low+1:high]
        cur_sol = solve_seq(cur_exp)
        last = expression[-1]
        expression = expression[0:low] + cur_sol + expression[high+1:-1] + last
    finals.append(int(expression[:-1]))
print(sum(finals))

#part 2

def solve_seq(expression):
    exp = expression.split("*")
    for i, part in enumerate(exp):
        if(part.count("+") > 0):
            exp[i] = str(eval(part))
    return str(eval("*".join(exp)))

finals = []
for expression in expressions:
    expression = "(" + expression + ")"
    while(not expression[:-1].isdigit() and expression[-1] == ")"):
        low, high = find_inner_par(expression)
        cur_exp = expression[low+1:high]
        cur_sol = solve_seq(cur_exp)
        last = expression[-1]
        expression = expression[0:low] + cur_sol + expression[high+1:-1] + last
    finals.append(int(expression[:-1]))
print(sum(finals))



    
    
    
    

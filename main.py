from itertools import product
from datetime import date
from math import sqrt

dailyDigits = ["2", "4", "0", "0"]
operators = ["+", "-", "*", "/", 'p']

def get_digit_combos(digits, combos, currCombo):
    if digits == []:
        # print(currCombo, combos)
        return currCombo
    n = 1
    numDigits = len(digits)
    for _ in range(numDigits):
        currCombo.append("".join(digits[:n])) # join the first n digits
        currComboCopy = currCombo.copy()[:-1] # get the old combo without the last element
        currCombo = get_digit_combos(digits[n:], combos, currCombo)
        if currCombo:
            # print(currCombo)
            combos.append(currCombo)
        currCombo = currComboCopy
        n += 1
    return None

def create_formula(numbers, signs, roots, operators):
    formula = ""
    for i in range(len(numbers)):
        if roots[i]:
            formula += sign[i] + "sqrt(" + numbers[i] + ")"
        else:
            formula += sign[i] + numbers[i]
        if i != len(numbers) - 1:
            # len(operators) == len(numbers) - 1
            formula += operators[i]
    formula = formula.replace("p", "**")
    return formula

combos = []
_ = get_digit_combos(dailyDigits, combos, [])
# print(combos)

# signs = {}
# for i in range(5):
#     signs[i] = list(product(["","-"], repeat=i))
signs = {0: [()], 1: [('',), ('-',)], 2: [('', ''), ('', '-'), ('-', ''), ('-', '-')], 3: [('', '', ''), ('', '', '-'), ('', '-', ''), ('', '-', '-'), ('-', '', ''), ('-', '', '-'), ('-', '-', ''), ('-', '-', '-')], 4: [('', '', '', ''), ('', '', '', '-'), ('', '', '-', ''), ('', '', '-', '-'), ('', '-', '', ''), ('', '-', '', '-'), ('', '-', '-', ''), ('', '-', '-', '-'), ('-', '', '', ''), ('-', '', '', '-'), ('-', '', '-', ''), ('-', '', '-', '-'), ('-', '-', '', ''), ('-', '-', '', '-'), ('-', '-', '-', ''), ('-', '-', '-', '-')]}

# sqrts = {}
# for i in range(5):
#     sqrts[i] = list(product([False, True], repeat=i))
sqrts = {0: [()], 1: [(False,), (True,)], 2: [(False, False), (False, True), (True, False), (True, True)], 3: [(False, False, False), (False, False, True), (False, True, False), (False, True, True), (True, False, False), (True, False, True), (True, True, False), (True, True, True)], 4: [(False, False, False, False), (False, False, False, True), (False, False, True, False), (False, False, True, True), (False, True, False, False), (False, True, False, True), (False, True, True, False), (False, True, True, True), (True, False, False, False), (True, False, False, True), (True, False, True, False), (True, False, True, True), (True, True, False, False), (True, True, False, True), (True, True, True, False), (True, True, True, True)]}

# operators = {}
# for i in range(4):
#     ps = list(product(operators, repeat=i))
#     print(ps)
#     perms = list(filter(lambda opList : opList.count('p') <= 1, ps))
#     operators[i] = perms
operators = {0: [()], 1: [('+',), ('-',), ('*',), ('/',), ('p',)], 2: [('+', '+'), ('+', '-'), ('+', '*'), ('+', '/'), ('+', 'p'), ('-', '+'), ('-', '-'), ('-', '*'), ('-', '/'), ('-', 'p'), ('*', '+'), ('*', '-'), ('*', '*'), ('*', '/'), ('*', 'p'), ('/', '+'), ('/', '-'), ('/', '*'), ('/', '/'), ('/', 'p'), ('p', '+'), ('p', '-'), ('p', '*'), ('p', '/')], 3: [('+', '+', '+'), ('+', '+', '-'), ('+', '+', '*'), ('+', '+', '/'), ('+', '+', 'p'), ('+', '-', '+'), ('+', '-', '-'), ('+', '-', '*'), ('+', '-', '/'), ('+', '-', 'p'), ('+', '*', '+'), ('+', '*', '-'), ('+', '*', '*'), ('+', '*', '/'), ('+', '*', 'p'), ('+', '/', '+'), ('+', '/', '-'), ('+', '/', '*'), ('+', '/', '/'), ('+', '/', 'p'), ('+', 'p', '+'), ('+', 'p', '-'), ('+', 'p', '*'), ('+', 'p', '/'), ('-', '+', '+'), ('-', '+', '-'), ('-', '+', '*'), ('-', '+', '/'), ('-', '+', 'p'), ('-', '-', '+'), ('-', '-', '-'), ('-', '-', '*'), ('-', '-', '/'), ('-', '-', 'p'), ('-', '*', '+'), ('-', '*', '-'), ('-', '*', '*'), ('-', '*', '/'), ('-', '*', 'p'), ('-', '/', '+'), ('-', '/', '-'), ('-', '/', '*'), ('-', '/', '/'), ('-', '/', 'p'), ('-', 'p', '+'), ('-', 'p', '-'), ('-', 'p', '*'), ('-', 'p', '/'), ('*', '+', '+'), ('*', '+', '-'), ('*', '+', '*'), ('*', '+', '/'), ('*', '+', 'p'), ('*', '-', '+'), ('*', '-', '-'), ('*', '-', '*'), ('*', '-', '/'), ('*', '-', 'p'), ('*', '*', '+'), ('*', '*', '-'), ('*', '*', '*'), ('*', '*', '/'), ('*', '*', 'p'), ('*', '/', '+'), ('*', '/', '-'), ('*', '/', '*'), ('*', '/', '/'), ('*', '/', 'p'), ('*', 'p', '+'), ('*', 'p', '-'), ('*', 'p', '*'), ('*', 'p', '/'), ('/', '+', '+'), ('/', '+', '-'), ('/', '+', '*'), ('/', '+', '/'), ('/', '+', 'p'), ('/', '-', '+'), ('/', '-', '-'), ('/', '-', '*'), ('/', '-', '/'), ('/', '-', 'p'), ('/', '*', '+'), ('/', '*', '-'), ('/', '*', '*'), ('/', '*', '/'), ('/', '*', 'p'), ('/', '/', '+'), ('/', '/', '-'), ('/', '/', '*'), ('/', '/', '/'), ('/', '/', 'p'), ('/', 'p', '+'), ('/', 'p', '-'), ('/', 'p', '*'), ('/', 'p', '/'), ('p', '+', '+'), ('p', '+', '-'), ('p', '+', '*'), ('p', '+', '/'), ('p', '-', '+'), ('p', '-', '-'), ('p', '-', '*'), ('p', '-', '/'), ('p', '*', '+'), ('p', '*', '-'), ('p', '*', '*'), ('p', '*', '/'), ('p', '/', '+'), ('p', '/', '-'), ('p', '/', '*'), ('p', '/', '/')]}

powers = {0: [()], 1: [('',), ('p',)], 2: [('', ''), ('p', ''), ('', 'p')], 3: [('', '', ''), ('p', '', ''), ('', 'p', ''), ('', '', 'p')], 4: [('', '', '', ''), ('p', '', '', ''), ('', 'p', '', ''), ('', '', 'p', ''), ('', '', '', 'p')]}

results = {}
with open(date.today().strftime("%Y-%m-%d") + ".txt", "w+") as f:
    for combo in combos:
        for sign in signs[len(combo)]:
                for root in sqrts[len(combo)]:
                    for operator in operators[len(combo)-1]:
                        formula = create_formula(combo, sign, root, operator)
                        try:
                            result = eval(formula)
                            if float(result).is_integer() and (result not in results or (result in results and len(formula) < len(results[result]))):
                                f.write(formula + "\n")
                                results[result] = formula
                        except:
                            pass


print(results[16])
print(results[-16])
print(results[5])
from datetime import date
import math

# dailyDigits = ["4", "6", "9", "7"]
# operators = ["+", "-", "*", "/", 'p']

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

def create_formula(numbers, sign, roots, operators):
    formula = ""
    raw = ""
    for i in range(len(numbers)):
        if roots[i]:
            formula += sign[i] + "math.sqrt(" + numbers[i] + ")"
            raw += sign[i] + "s" + numbers[i]
        else:
            formula += sign[i] + numbers[i]
            raw += sign[i] + numbers[i]
        if i != len(numbers) - 1:
            # len(operators) == len(numbers) - 1
            formula += operators[i]
            raw += operators[i]
    formula = formula.replace("p", "**")
    # if roots == (False, False, True, False):
    #     print(formula)
    return formula, raw

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

def generateResults(dailyDigits, writeResults=True):
    results = {}
    combos = []
    _ = get_digit_combos(dailyDigits, combos, [])
    with open(date.today().strftime("%Y-%m-%d") + ".txt", "w+") as f:
        for combo in combos:
            for sign in signs[len(combo)]:
                for root in sqrts[len(combo)]:
                    for operator in operators[len(combo)-1]:
                        formula, raw = create_formula(combo, sign, root, operator)
                        try:
                            result = eval(formula)
                            if float(result).is_integer() and -150 < result < 150 and (result not in results or (result in results and len(formula) < len(results[result]))):
                                f.write(formula + "=" + str(result) + "\n")
                                results[result] = raw
                        except Exception as e:
                            pass
    return results

if __name__ == "__main__":
    results = generateResults(['0', '2', '3', '0'], False)
    print(results[-8])
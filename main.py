from itertools import product
from datetime import date

dailyDigits = ["7", "4", "4", "8"]
operators = ["+", "-", "*", "/"]

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

def create_formula(sign, digits, operators):
    formula = ""
    for i in range(len(digits)):
        formula += sign[i] + digits[i]
        if i != len(digits) - 1:
            formula += operators[i]
    return formula

combos = []
_ = get_digit_combos(dailyDigits, combos, [])
# print(combos)

signs = {}
for i in range(5):
    signs[i] = list(product(["","-"], repeat=i))

operatorPerms = {}
for i in range(4):
    operatorPerms[i] = list(product(operators, repeat=i))

results = {}
with open(date.today().strftime("%Y-%m-%d") + ".txt", "w+") as f:
    for combo in combos:
        for sign in signs[len(combo)]:
            for operatorPerm in operatorPerms[len(combo)-1]:
                formula = create_formula(sign, combo, operatorPerm)
                result = eval(formula)
                if float(result).is_integer():
                    f.write(formula + "\n")
                    results[result] = formula

print(results[7])
print(results[-32])
print(results[-93])
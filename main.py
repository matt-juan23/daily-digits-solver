import os
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from daily_digits_solver import generateResults

def getElementByCSSPath(path):
    element = WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, path)))
    return element

def getElementByID(id):
    element = WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.ID, id)))
    return element

def getDailyDigits():
    dailyDigits = []
    for i in range(1,5):
        dailyDigits.append(getElementByID("b" + str(i)).text)
    return dailyDigits

def enterSolution(formula):
    num = 1
    for value in formula:
        # time.sleep(0.5)
        if value.isnumeric():
            getElementByID("b"+str(num)).click()
            num += 1
        else:
            getElementByID(mapping[value]).click()
    getElementByID("bsubmit").click()

mapping = {"+": "bplus", "-": "bminus", "*": "bmultiply", "/": "bdivide", "s": "broot", "p": "bpower", ")": "bclose"}

username = ""
password = ""

if username == "" or password == "":
    print("USERNAME OR PASSWORD IS NOT SET")
    exit()

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
browser = webdriver.Chrome(options=chrome_options)
browser.get("https://dailydigits.today/index1.php")
getElementByCSSPath("div.form-group:nth-child(3) > input:nth-child(2)").send_keys(username)
getElementByCSSPath("div.form-group:nth-child(4) > input:nth-child(2)").send_keys(password)
getElementByCSSPath(".btn").click()

time.sleep(1)
getElementByCSSPath("#modalInstructions > div.modal-header > button").click()
dailyDigits = getDailyDigits()
results = generateResults(dailyDigits)
for _ in range(3):
    # time.sleep(1)
    target = int(getElementByCSSPath("#current").text)
    enterSolution(results[target])

import random
import time
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

names = ["jay", "jim", "roy", "axel", "billy", "charlie", "jax", "gina", "paul",
"ringo", "ally", "nicky", "cam", "ari", "trudie", "cal", "carl", "lady", "lauren",
"ichabod", "arthur", "ashley", "drake", "kim", "julio", "lorraine", "floyd", "janet",
"lydia", "charles", "pedro", "bradley"]
numbers = ['1','2','3','4','5','6','7','8','9','0']

link = 'https://my.asos.com/identity/register?lang=en-GB&store=COM&country=GB&keyStoreDataversion=dup0qtf-35&returnUrl=https%3A%2F%2Fwww.asos.com%2Fmen%2F'

file = open('account.txt','w')
password = input("Enter password: ")
catchall = input("Enter catchall (Along with @ symbol, e.g. @table.com):")
s = Service(r"C:\Users\[User]\Desktop\asos\chromedriver\chromedriver.exe")
options = Options()
#options = webdriver.ChromeOptions()
options.headless
driver = webdriver.Chrome(service=s,options=options)

driver.get(link)

fName = random.choice(names)
lName = random.choice(names)


nLength = 2
num = ''.join(random.choice(numbers) for i in range(nLength))
email = str(fName)+str(lName)+str(num)+catchall
passw = password

select1 = Select(driver.find_element(By.XPATH, '//*[@id="BirthDay"]'))
select2 = Select(driver.find_element(By.XPATH, '//*[@id="BirthMonth"]'))
select3 = Select(driver.find_element(By.XPATH, '//*[@id="BirthYear"]'))


driver.find_element(By.XPATH, '//*[@id="Email"]').send_keys(email)
driver.find_element(By.XPATH, '//*[@id="FirstName"]').send_keys(fName)
driver.find_element(By.XPATH, '//*[@id="LastName"]').send_keys(lName)
driver.find_element(By.XPATH, '//*[@id="Password"]').send_keys(passw)
select1.select_by_visible_text('1')
select2.select_by_visible_text('January')
select3.select_by_visible_text('2000')
driver.find_element(By.XPATH, '//*[@id="register"]').click()
file.write(str(email) + ':' + str(password))
file.close()
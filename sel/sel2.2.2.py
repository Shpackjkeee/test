from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

link = "https://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element(By.CSS_SELECTOR, "#num1")
input2 = browser.find_element(By.CSS_SELECTOR, "#num2")
n1 = input1.text 
n2 = input2.text 

s_12 = int(n1) + int(n2)

select = Select(browser.find_element(By.CLASS_NAME, "custom-select"))
l = str(s_12)
select.select_by_value(l)

button = browser.find_element(By.CSS_SELECTOR, "btn-default")
send_button.click()

time.sleep(15)


browser.quit()
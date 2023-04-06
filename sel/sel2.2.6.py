from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math

link = "https://SunInJuly.github.io/execute_script.html"

browser = webdriver.Chrome()

browser.get(link)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
x = x_element.text
y = calc(x) 

input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
browser.execute_script("window.scrollBy(0, 150);")
input1.send_keys(y)

button = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
button.click()   

button = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
button.click() 

button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()



time.sleep(15)

browser.quit()



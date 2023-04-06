from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math
import os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

browser.switch_to.window(browser.window_handles[1])

x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
x = x_element.text
y = calc(x)

input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
#browser.execute_script("window.scrollBy(0, 150);")
input1.send_keys(y)


button = browser.find_element(By.CSS_SELECTOR, "button.btn-primary")
button.click()



time.sleep(30)


    #button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    #button.click()



    #time.sleep(15)

browser.quit()



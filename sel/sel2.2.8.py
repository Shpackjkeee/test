from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math
import os

link = "https://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element(By.NAME, 'firstname')
input1.send_keys("Viacheslav")
input2 = browser.find_element(By.NAME, 'lastname')
input2.send_keys("Slavniy")
input3 = browser.find_element(By.NAME, 'email')
input3.send_keys("stepik@gogo.ru")

element = browser.find_element(By.CSS_SELECTOR, "#file")

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 

element.send_keys(file_path)

button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()



time.sleep(30)


    #button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    #button.click()



    #time.sleep(15)

browser.quit()



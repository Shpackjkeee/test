from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

link = "file:///C:/Users/111/test/sel/forma.html"
browser = webdriver.Chrome()
browser.get(link)


input1 = browser.find_element(By.NAME, "FIO")
input1.send_keys("Viacheslav")
input2 = browser.find_element(By.NAME, "email")
input2.send_keys("Slavniy")
input3 = browser.find_element(By.NAME, "Phone") 
input3.send_keys("Slavniy")

select1 = Select(browser.find_element(By.NAME, "transfer"))
select1.select_by_value("Да") # ищем элемент с текстом "Python"
select2 = Select(browser.find_element(By.NAME, "HowManyPeople"))
select2.select_by_value("1") # ищем элемент с текстом "Python"
select3 = Select(browser.find_element(By.NAME, "HowManyChild"))
select3.select_by_value("3") # ищем элемент с текстом "Python"
input5 = browser.find_element(By.NAME, "ChildAge")
input5.send_keys("3, 25, 3")


button = browser.find_element(By.CSS_SELECTOR, "button.btn")

time.sleep(12)

browser.quit()
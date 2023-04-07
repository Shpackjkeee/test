import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestAbs(unittest.TestCase):
    def test_abs1(self):
        link = "https://suninjuly.github.io/registration1.html"   
        browser = webdriver.Chrome()
        browser.get(link) 
        input1 = browser.find_element(By.CSS_SELECTOR, 'input.first[required]')
        input1.send_keys("Viacheslav")
        input2 = browser.find_element(By.CSS_SELECTOR, 'input.second[required]')
        input2.send_keys("Slavniy")
        input3 = browser.find_element(By.CSS_SELECTOR, 'input.third')
        input3.send_keys("slava@mail.ru")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        browser.implicitly_wait(5)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    def test_abs2(self):
        link = "https://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link) 
        input1 = browser.find_element(By.CSS_SELECTOR, 'input.first[required]')
        input1.send_keys("Viacheslav")
        input2 = browser.find_element(By.CSS_SELECTOR, 'input.second[required]')
        input2.send_keys("Slavniy")
        input3 = browser.find_element(By.CSS_SELECTOR, 'input.third')
        input3.send_keys("slava@mail.ru")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        browser.implicitly_wait(5)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, msg="Errr")

if __name__ == "__main__":
    unittest.main()
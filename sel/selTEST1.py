from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    #Link
try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    #Поиск
    x_element = browser.find_element(By.CSS_SELECTOR, '[id="treasure"]')
    x_element = x_element.get_attribute("valuex")
    x = x_element
    y = calc(x)

    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(y)

    option1 = browser.find_element(By.CSS_SELECTOR, '[id="robotCheckbox"]')
    option1.click()

    robots_radio = browser.find_element(By.ID, "robotsRule")
    robots_checked = robots_radio.get_attribute("checked")
    assert robots_checked is None

    option3 = browser.find_element(By.CSS_SELECTOR, '[id="robotsRule"]')
    option3.click()


    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(10)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

     # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
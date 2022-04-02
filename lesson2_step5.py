from selenium import webdriver
import time
import math


try:
    def calc(a):
        return str(math.log(abs(12 * math.sin(int(x)))))

    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # находим элемент, содержащий текст
    x_text_elt = browser.find_element_by_id("input_value")
    # записываем в переменную x текст из элемента welcome_text_elt
    x = x_text_elt.text
    y = calc(int(x))

    # Ваш код, который заполняет обязательные поля
    input_x = browser.find_element_by_id('answer')
    input_x.send_keys(y)

    check_robot = browser.find_element_by_css_selector('[for="robotCheckbox"]')
    check_robot.click()

    radio_robot = browser.find_element_by_css_selector('[for="robotsRule"]')
    radio_robot.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
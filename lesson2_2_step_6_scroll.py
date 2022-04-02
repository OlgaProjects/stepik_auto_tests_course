from selenium import webdriver
import time
import math


try:
    def calc(a):
        return str(math.log(abs(12 * math.sin(int(a)))))

    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    number_elt = browser.find_element_by_id("input_value")
    number = number_elt.text
    print(number)
    y = calc(int(number))

    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    inp1 = browser.find_element_by_id('answer')
    inp1.send_keys(y)

    check_robot = browser.find_element_by_css_selector('[for="robotCheckbox"]')
    check_robot.click()

    radio_robot = browser.find_element_by_css_selector('[for="robotsRule"]')
    radio_robot.click()

    # button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
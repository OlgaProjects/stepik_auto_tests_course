from selenium import webdriver
import time
import math


try:
    def calc(a):
        return str(math.log(abs(12 * math.sin(int(a)))))

    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    treasure_elt = browser.find_element_by_id("treasure")
    treasure_checked = treasure_elt.get_attribute("valuex")
    print(treasure_checked)
    y = calc(int(treasure_checked))

    inp1 = browser.find_element_by_id('answer')
    inp1.send_keys(y)

    check_robot = browser.find_element_by_id('robotCheckbox')
    check_robot.click()

    radio_robot = browser.find_element_by_id('robotsRule')
    radio_robot.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
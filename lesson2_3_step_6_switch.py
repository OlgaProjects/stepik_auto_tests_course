from selenium import webdriver
import math
import time

try:
    def calc(a):
        return str(math.log(abs(12 * math.sin(int(a)))))

    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.execute_script("document.getElementsByTagName('button')[0].classList.remove('trollface');")

    button = browser.find_element_by_tag_name("button")
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    # confirm = browser.switch_to.alert
    #  confirm.accept()

    number_elt = browser.find_element_by_id("input_value")
    number = number_elt.text
    print(number)
    y = calc(int(number))

    inp1 = browser.find_element_by_id('answer')
    inp1.send_keys(y)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
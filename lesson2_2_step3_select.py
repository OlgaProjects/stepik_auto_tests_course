from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

try:

    link = " http://suninjuly.github.io/selects1.html"  #http://suninjuly.github.io/selects2.html
    browser = webdriver.Chrome()
    browser.get(link)

    x_text_elt = browser.find_element_by_id("num1")
    y_text_elt = browser.find_element_by_id("num2")

    x = int(x_text_elt.text)
    y = int(y_text_elt.text)
    result = str(x + y)
    print(result)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(result)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

#
# driver = webdriver.Chrome()
# driver.get("https://SunInJuly.github.io/execute_script.html")
#
# try:
#     button = driver.find_element_by_tag_name("button")
#     _ = button.location_once_scrolled_into_view
#
#     button.click()
#     assert True
# finally:
#     driver.quit()

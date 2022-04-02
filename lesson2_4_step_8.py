from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

try:

    def calc(a):
        return str(math.log(abs(12 * math.sin(int(a)))))

    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    text_price = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "100")
        )
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    number_elt = browser.find_element_by_id("input_value")
    number = number_elt.text
    print(number)
    y = calc(int(number))

    inp1 = browser.find_element_by_id('answer')
    inp1.send_keys(y)

    button_solve = browser.find_element_by_id("solve")
    button_solve.click()

finally:

    browser.quit()
# # говорим Selenium проверять в течение 5 секунд пока кнопка станет неактивной
# button = WebDriverWait(browser, 5).until_not(
#         EC.element_to_be_clickable((By.ID, "verify"))
#     )
#
# assert "successful" in message.text
import os
from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input_first_name = browser.find_element_by_name("firstname")
    input_first_name.send_keys("Ivan")
    input_last_name = browser.find_element_by_name("lastname")
    input_last_name.send_keys("Ivanov")
    input_email = browser.find_element_by_name("email")
    input_email.send_keys("supermail_ivanov@gmail.com")

    with open('test1.txt', 'w') as file:
        file.write('test1 for mls 228')
    path = os.getcwd() + '/' + file.name

    # current_dir = os.getcwd()
    # print(current_dir)
    # file_name = "test_file.txt"
    # file_path = os.path.join(current_dir, file_name)
    print(path)

    element = browser.find_element_by_css_selector("[type='file']")
    element.send_keys(path)

    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

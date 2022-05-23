import time

try:

    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

    def test_add_busket_button_pass(browser):
        browser.get(link)
        add_busket_button = browser.find_element_by_class_name("btn.btn-lg.btn-primary.btn-add-to-basket")
        # text_element_button = element_button.text
        assert add_busket_button, 'Кнопка добавления в корзину не найдена'
finally:
    time.sleep(5)
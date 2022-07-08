from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


# команды для запуска с различными настройками
# pytest -s -v --language=en test_items.py
# pytest -s -v --language=ru test_items.py
# pytest -s -v --language=es test_items.py
# pytest -s -v --browser_name=firefox --language=fr test_items.py

def test_button_is_on_page(browser):
    browser.get(link)
    button = browser.find_element(By.CLASS_NAME, "btn-primary")
    print(button.text)  # вывожу название кнопки в терминал и не использую time.sleep()

    assert type(button) == WebElement, 'Кнопки купить нет на странице'

from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
# from .login_page import LoginPage
from .locators import BaseLocators
import math


class BasePage():
    # конструктор - метод, который вызывается, когда мы создаем объект
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    # метод, открывающий нужную страницу в браузере
    def open(self):
        self.browser.get(self.url)

    # Переход в корзину
    def go_to_basket_page(self):
        basket_button = self.browser.find_element(*BaseLocators.BASKET_BUTTON)
        basket_button.click()

    # Переход на страницу авторизации
    def go_to_login_page(self):
        login_link = self.browser.find_element(*BaseLocators.LOGIN_LINK)
        login_link.click()
        # return LoginPage(browser=self.browser, url=self.browser.current_url)

    # Проверка на наличии кнопки перехода на страницу авторизации
    def should_be_login_link(self):
        assert self.is_element_present(*BaseLocators.LOGIN_LINK), 'Login link is not presented'

    # метод перехватывающий исключения
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    # метод проверяющий, что элемент не появляется на странице в течении заданного времени
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    # метод проверяющий, что элемент исчезает
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    # Метод для расчета математического выражения (нужен в некоторых тестах)
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

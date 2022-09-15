from selenium.common.exceptions import NoSuchElementException


class BasePage():

    # конструктор - метод, который вызывается, когда мы создаем объект
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    # метод, открывающий нужную страницу в браузере
    def open(self):
        self.browser.get(self.url)

    # метод перехватывающий исключения
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

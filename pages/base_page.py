class BasePage():

    # конструктор - метод, который вызывается, когда мы создаем объект
    def __int__(self, browser, url):
        self.browser = browser
        self.url = url

    # метод, открывающий нужную страницу в браузере
    def open(self):
        self.browser.get(self.url)


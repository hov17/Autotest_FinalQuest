from .pages.login_page import LoginPage


def test_should_be_login_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/accounts/login/'
    page = LoginPage(browser, link, timeout=10)
    page.open()
    page.should_be_login_page()

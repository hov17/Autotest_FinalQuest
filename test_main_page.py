from .pages.main_page import MainPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link, timeout=10)
    page.open()
    page.go_to_login_page()


def test_guest_should_be_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link, timeout=10)
    page.open()
    page.should_be_login_link()

import pytest
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage


#  В параметрах указываем различные промо. 7-ое промо заведомо падающее
@pytest.mark.parametrize('num', [*range(7), pytest.param(7, marks=pytest.mark.xfail(reason='Bugged')),
                                 *range(8, 10)])
# Тест на добавление товара в корзину и проверку сообщений
def test_guest_can_add_product_to_basket(browser, num):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{num}'
    page = ProductPage(browser, link, timeout=5)
    page.open()
    page.product_add_to_basket()
    page.solve_quiz_and_get_code()
    page.product_add_to_basket_success()


# Наличие кнопки перехода на страницу авторизации
def test_guest_should_see_login_link_on_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/'
    page = ProductPage(browser, link, timeout=10)
    page.open()
    page.should_be_login_link()


# Переход на страницу авторизации
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/'
    page = ProductPage(browser, link, timeout=10)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url, timeout=10)
    login_page.should_be_login_page()


# Нет сообщения о добавлении товара в корзину
@pytest.mark.xfail(reason='После добавления товара, сообщение отображается')
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
    page = ProductPage(browser, link)
    page.open()
    page.product_add_to_basket()
    page.should_not_be_success_message()


# Нет сообщения о добавлении товара в корзину при открытии страницы
def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


# Сообщение о добавлении товара в корзину должно исчезнуть
@pytest.mark.xfail(reason='Сообщение не исчезает')
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
    page = ProductPage(browser, link)
    page.open()
    page.product_add_to_basket()
    page.success_message_should_be_disappeared()

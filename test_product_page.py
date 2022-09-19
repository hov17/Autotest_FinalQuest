import pytest
from .pages.product_page import ProductPage


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

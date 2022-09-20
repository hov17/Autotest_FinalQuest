from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    # В корзине отсутствует товар
    def basket_should_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_PRODUCT_FORM), 'В корзине есть товар!'

    # Сообщение о том, что корзина пуста
    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), \
            'Сообщение о том, что корзина пуста, отсутствует!'

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def product_add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_CART)
        button.click()

    def product_add_to_basket_success(self):
        self.message_of_success_added_book()
        self.message_of_success_added_book_with_price()
        self.correct_name_of_added_book()
        self.correct_price_of_added_book()

    def message_of_success_added_book(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_OF_SUCCESS_ADDED_BOOK),\
            'Сообщение о добавлении книги в корзину отсутствует!'

    def message_of_success_added_book_with_price(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_OF_SUCCESS_ADDED_BOOK_WITH_PRICE),\
            'Сообщение с ценой о добавлении книги в корзину отсутствует'

    def correct_name_of_added_book(self):
        name_of_book = self.browser.find_element(*ProductPageLocators.NAME_OF_BOOK)
        name_of_book = name_of_book.text
        name_of_book_in_message = self.browser.find_element(*ProductPageLocators.NAME_OF_BOOK_IN_MESSAGE)
        name_of_book_in_message = name_of_book_in_message.text
        assert name_of_book == name_of_book_in_message, 'Название книги не совпадают!'

    def correct_price_of_added_book(self):
        price_of_book = self.browser.find_element(*ProductPageLocators.PRICE_OF_BOOK)
        price_of_book = price_of_book.text
        price_of_book_in_message = self.browser.find_element(*ProductPageLocators.PRICE_OF_BOOK_IN_MESSAGE)
        price_of_book_in_message = price_of_book_in_message.text
        assert price_of_book == price_of_book_in_message, 'Цена книги не совпадает!'

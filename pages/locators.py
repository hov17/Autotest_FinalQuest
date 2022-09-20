from selenium.webdriver.common.by import By


# Базовые локаторы
class BaseLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link_inc')
    BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-group :nth-child(1).btn-default')


# Локаторы страницы с корзиной
class BasketPageLocators():
    BASKET_PRODUCT_FORM = (By.CSS_SELECTOR, '#basket_formset')
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, '#content_inner > p')


# Локаторы для главной страницы
class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


# Локаторы для страницы авторизации
class LoginPageLocators():
    REGISTRATION_FROM = (By.ID, 'register_form')
    LOGIN_FORM = (By.ID, 'login_form')


# Локаторы для страницы товаров
class ProductPageLocators():
    BUTTON_ADD_TO_CART = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    MESSAGE_OF_SUCCESS_ADDED_BOOK = (By.CSS_SELECTOR, '#messages :nth-child(1).alert')
    MESSAGE_OF_SUCCESS_ADDED_BOOK_WITH_PRICE = (By.CSS_SELECTOR, '#messages :nth-child(1).alert')
    NAME_OF_BOOK = (By.CSS_SELECTOR, '#content_inner h1')
    NAME_OF_BOOK_IN_MESSAGE = (By.CSS_SELECTOR, '#messages :nth-child(1) > .alertinner strong')
    PRICE_OF_BOOK = (By.CSS_SELECTOR, '#content_inner p')
    PRICE_OF_BOOK_IN_MESSAGE = (By.CSS_SELECTOR, '#content_inner .product_main .price_color')

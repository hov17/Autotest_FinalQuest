from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators():
    REGISTRATION_FROM = (By.ID, 'register_form')
    LOGIN_FORM = (By.ID, 'login_from')

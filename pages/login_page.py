from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    # Метод для регистрации пользователя
    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.EMAIL_REGISTER_FIELD).send_keys(email)
        self.browser.find_element(*LoginPageLocators.PASSWORD1_REGISTER_FIELD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.PASSWORD2_REGISTER_FIELD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()

    # Общая проверка страницы авторизации
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    # Проверка правильного адреса
    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, 'Wrong page!'

    # Проверка наличия формы авторизации
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Login form is missing!'

    # Проверка наличия формы регистрации
    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FROM), 'Registration form is missing!'

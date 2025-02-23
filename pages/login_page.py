import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as ec


class LoginPage(BasePage):

    PAGE_URL = Links.LOGIN_PAGE

    USERNAME_FIELD = ("xpath", "//input[@name = 'username']")
    PASSWORD_FIELD = ("xpath", "//input[@name = 'password']")
    SUBMIT_BUTTON = ("xpath", "//button[@type= 'submit']")

    @allure.step("Enter login")
    def enter_login(self, login): # функция ввода логина
        self.wait.until(ec.element_to_be_clickable(self.USERNAME_FIELD)).send_keys(login) # явное ожидание

    @allure.step("Enter password")
    def enter_password(self, password): # функция ввода пароля
        self.wait.until(ec.element_to_be_clickable(self.PASSWORD_FIELD)).send_keys(password)

    @allure.step("Click on submit button")
    def click_submit_button(self): # функция нажатия на кнопку
        self.wait.until(ec.element_to_be_clickable(self.SUBMIT_BUTTON)).click()

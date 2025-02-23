#import time
import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import Keys


class PersonalPage(BasePage):

    PAGE_URL = Links.PERSONAL_PAGE
    FIRST_NAME_FIELD = ("xpath", "//input[@name='firstName']")
    SAVE_BUTTON = ("xpath", "(//button[@type='submit'])[1]") # Выбираем первую кнопку сохранения
    SPINNER = ("xpath", "//div[@class ='oxd-loading-spinner']")


    def change_name(self, new_name):
        with allure.step(f"Change name on {new_name}"): # Применяется with, если в маркере требуется вывести переменную
            first_name_field = self.wait.until(ec.element_to_be_clickable(self.FIRST_NAME_FIELD))  # ищем поле
            first_name_field.send_keys(Keys.CONTROL + "A")  # command для IOS
            first_name_field.send_keys(Keys.BACKSPACE)
            first_name_field.send_keys(new_name)  # ввод нового имени
            self.name = new_name

    @allure.step("Save first name")
    def save_changes(self):
        self.wait.until(ec.element_to_be_clickable(self.SAVE_BUTTON)).click() # Сохранение изменений

    @allure.step("Changes have been saved successfully")
    def is_changes_saved(self):
        self.wait.until(ec.invisibility_of_element(self.SPINNER)) # Ждем исчезновение спиннера
        self.wait.until(ec.visibility_of_element_located(self.FIRST_NAME_FIELD)) # Ждем появление поля
        self.wait.until(ec.text_to_be_present_in_element_value(self.FIRST_NAME_FIELD, self.name)) # Проверяем значение

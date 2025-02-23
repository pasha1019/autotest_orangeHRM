import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10, poll_frequency=1) # указываем явное ожидание

    def open(self):
        with allure.step(f"Open {self.PAGE_URL}"): # Устанавливаем allure маркер
            self.driver.get(self.PAGE_URL) # открытие страницы, URL прописан индивидуально


    def is_opened(self): # проверка открытия страницы
        with allure.step(f"Page {self.PAGE_URL} is opened"):  # Устанавливаем allure маркер
            self.wait.until(ec.url_to_be(self.PAGE_URL))

    def make_screenshot(self, screenshot_name):
        allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name=screenshot_name,
            attachment_type=AttachmentType.PNG
                      )

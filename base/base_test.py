import pytest

from pages.login_page import LoginPage
from pages.personal_page import PersonalPage
from pages.dashboard_page import DashboardPage
from config.data import Data


class BaseTest:

    data: Data # Аннотация типов

    login_page: LoginPage
    dashboard_page: DashboardPage
    personal_page: PersonalPage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.data = Data()

        request.cls.login_page = LoginPage(driver) # Создаем объекты страниц
        request.cls.dashboard_page = DashboardPage(driver)
        request.cls.personal_page = PersonalPage(driver)

import random
import pytest
import allure

from base.base_test import BaseTest


@allure.feature("Profile functions")
class TestProfileFeature(BaseTest):

    @allure.title("Change profile name")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_change_profile_name(self):
        self.login_page.open() # Открыли страницу
        self.login_page.enter_login(self.data.LOGIN) # Ввели логин
        self.login_page.enter_password(self.data.PASSWORD)  # Ввели пароль
        self.login_page.click_submit_button() # Нажимаем авторизоваться
        self.dashboard_page.is_opened() # Проверили, что открылся дашборд
        self.dashboard_page.click_my_info_link() # Перешли на страницу my_info
        self.personal_page.is_opened() # Проверили, что страница my_info открыта
        self.personal_page.change_name(f"Test {random.randint(1,100)}") # Изменили имя
        self.personal_page.save_changes() # Сохранили изменения
        self.personal_page.is_changes_saved() # Проверили, что изменения сохранены
        self.personal_page.make_screenshot("Success") # Делаем симок

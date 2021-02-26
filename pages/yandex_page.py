from .base_page import BasePage
from .locators import YandexPageLocators

class YandexPage(BasePage):

    def should_be_find_button(self):
        # Проверяем наличия кнопки "Найти" на странице
        assert self.is_element_present(*YandexPageLocators.FIND_BUTTON), "Check button 'Найти' on Page!"
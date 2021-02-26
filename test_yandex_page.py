import pytest

from .pages.main_page import MainPage
from .pages.yandex_page import YandexPage
from .pages.locators import YandexPageLocators

@pytest.mark.yandex
def test_yandex_page(browser):
    link = YandexPageLocators.YANDEX_PAGE_LINK
    page = MainPage(browser, link)
    page.open()
    yandex_page = YandexPage(browser, browser.current_url)
    yandex_page.should_be_find_button()
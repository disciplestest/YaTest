from selenium.webdriver.common.by import By


class YandexPageLocators():
    YANDEX_PAGE_LINK = 'https://yandex.ru/'
    FIND_BUTTON = (By.CSS_SELECTOR, ".button.mini-suggest__button.button_theme_websearch.button_size_ws-head.i-bem.button_js_inited")
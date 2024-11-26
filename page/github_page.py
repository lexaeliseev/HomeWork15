import time

import allure
from selene import browser, be


class GitHubPage:
    def __init__(self):
        pass

    @staticmethod
    def sign_in_desktop():
        with allure.step('Клик по кнопке sign-up'):
            browser.element('.HeaderMenu-link--sign-up').click()

        with allure.step('Поле Email отображается на странице'):
            browser.element('[name="user[email]"]').should(be.visible)

    def sign_in_mobile(self):
        with allure.step('Клик по кнопке burger menu'):
            browser.element(".Button--link").click()

        self.sign_in_desktop()

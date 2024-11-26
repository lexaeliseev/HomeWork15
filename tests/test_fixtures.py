"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""
import allure
from allure_commons.types import Severity
from selene import browser

import page.github_page

github_page = page.github_page.GitHubPage()


@allure.tag("web")
@allure.label("owner", "aa.eliseev")
@allure.severity(Severity.CRITICAL)
@allure.feature("Вход в GitHub")
@allure.story("Проверка входа в GitHub на десктопном разрешении экрана")
@allure.link("https://github.com", name="github")
def test_github_desktop(desktop_screen_setup):
    browser.open('/')
    github_page.sign_in_desktop()


@allure.tag("mobile")
@allure.label("owner", "aa.eliseev")
@allure.severity(Severity.CRITICAL)
@allure.feature("Вход в GitHub")
@allure.story("Проверка входа в GitHub на мобильном разрешении экрана")
@allure.link("https://github.com", name="github")
def test_github_mobile(mobile_screen_setup):
    browser.open('/')
    github_page.sign_in_mobile()

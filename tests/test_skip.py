"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
from selene import browser
from allure_commons.types import Severity
import allure

import page.github_page

github_page = page.github_page.GitHubPage()


@allure.tag("web")
@allure.label("owner", "aa.eliseev")
@allure.severity(Severity.CRITICAL)
@allure.feature("Вход в GitHub")
@allure.story("Проверка входа в GitHub на десктопном разрешении экрана")
@allure.link("https://github.com", name="github")
def test_github_desktop(mobile_and_desktop_screen_setup):
    if mobile_and_desktop_screen_setup == 'mobile':
        pytest.skip("Размер экрана для десктопного приложения")
    browser.open('/')
    github_page.sign_in_desktop()


@allure.tag("mobile")
@allure.label("owner", "aa.eliseev")
@allure.severity(Severity.CRITICAL)
@allure.feature("Вход в GitHub")
@allure.story("Проверка входа в GitHub на мобильном разрешении экрана")
@allure.link("https://github.com", name="github")
def test_github_mobile(mobile_and_desktop_screen_setup):
    if mobile_and_desktop_screen_setup == 'desktop':
        pytest.skip("Размер экрана для мобильного приложения")
    browser.open('/')
    github_page.sign_in_mobile()
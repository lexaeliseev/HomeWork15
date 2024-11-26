import allure
import pytest
from selene import browser
import page.github_page
from allure_commons.types import Severity

github_page = page.github_page.GitHubPage()


@allure.tag("web")
@allure.label("owner", "aa.eliseev")
@allure.severity(Severity.CRITICAL)
@allure.feature("Вход в GitHub")
@allure.story("Проверка входа в GitHub на десктопном разрешении экрана")
@allure.link("https://github.com", name="github")
@pytest.mark.parametrize('width, height', [(1920, 1080), (1024, 768), (1280, 720)])
def test_sign_in_desktop(width, height):
    browser.config.window_width = width
    browser.config.window_height = height

    browser.open("/")
    github_page.sign_in_desktop()


@allure.tag("mobile")
@allure.label("owner", "aa.eliseev")
@allure.severity(Severity.CRITICAL)
@allure.feature("Вход в GitHub")
@allure.story("Проверка входа в GitHub на мобильном разрешении экрана")
@allure.link("https://github.com", name="github")
@pytest.mark.parametrize('width, height', [(360, 800), (414, 896), (420, 800)])
def test_sign_in_mobile(width, height):
    browser.config.window_width = width
    browser.config.window_height = height

    browser.open("/")
    github_page.sign_in_mobile()


@allure.tag("web")
@allure.label("owner", "aa.eliseev")
@allure.severity(Severity.CRITICAL)
@allure.feature("Вход в GitHub")
@allure.story("Проверка входа в GitHub на десктопном разрешении экрана")
@allure.link("https://github.com", name="github")
@pytest.mark.parametrize('width, height', [(1920, 1080), (1024, 768), (1280, 720)],
                         ids=['desktop_1920x1080', 'desktop_1024x768', 'desktop_1280x1024'])
def test_sign_in_desktop_with_ids(width, height):
    browser.config.window_width = width
    browser.config.window_height = height

    browser.open("/")
    github_page.sign_in_desktop()


@allure.tag("mobile")
@allure.label("owner", "aa.eliseev")
@allure.severity(Severity.CRITICAL)
@allure.feature("Вход в GitHub")
@allure.story("Проверка входа в GitHub на мобильном разрешении экрана")
@allure.link("https://github.com", name="github")
@pytest.mark.parametrize('width, height', [(360, 800), (414, 896), (420, 800)],
                         ids=['mobile_360x800', 'mobile_414x896', 'mobile_420x800'])
def test_sign_in_mobile_with_ids(width, height):
    browser.config.window_width = width
    browser.config.window_height = height

    browser.open("/")
    github_page.sign_in_mobile()

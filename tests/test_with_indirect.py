import allure
import pytest
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
@pytest.mark.parametrize('desktop_screen_setup', [(1440, 900)], indirect=True)
def test_sign_in_desktop_with_indirect(desktop_screen_setup):
    browser.open('/')
    github_page.sign_in_desktop()

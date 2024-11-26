import pytest
from selene import browser


@pytest.fixture(scope='session', autouse=True)
def open_base_url():
    browser.config.base_url = 'https://github.com'
    yield
    browser.quit()
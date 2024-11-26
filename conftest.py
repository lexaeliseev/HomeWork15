import pytest
from selene import browser

from utils import attach


@pytest.fixture(scope='session', autouse=True)
def open_base_url():
    browser.config.base_url = 'https://github.com'
    yield

    attach.add_html(browser)
    attach.add_screenshot(browser)
    browser.quit()


@pytest.fixture(scope='function', params=[(1920, 1080), (1280, 1024), (1024, 768), (1440, 900)],
                ids=['desktop_1920x1080', 'desktop_1280x1024', 'desktop_1024x720', 'desktop_1440x900'])
def desktop_screen_setup(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height


@pytest.fixture(scope='function', params=[(360, 800), (414, 896), (420, 800)],
                ids=['mobile_360x800', 'mobile_414x896', 'mobile_420x800'])
def mobile_screen_setup(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height


@pytest.fixture(scope='function',
                params=[(360, 800), (1024, 768), (414, 896), (1920, 1080), (420, 800), (1280, 1024)],
                ids=['mobile_360x800', 'desktop_1024x768', 'mobile_414x896', 'desktop_1920x1080', 'mobile_420x800', 'desktop_1280x1024'])
def mobile_and_desktop_screen_setup(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height

    if width >= 1024:
        yield 'desktop'
    else:
        yield 'mobile'
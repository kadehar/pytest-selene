from selene.support.shared import browser
import pytest


@pytest.fixture(scope='session', autouse=True)
def setup():
    browser.open('data:')
    browser.driver.set_window_size(width=1920, height=1080)


@pytest.fixture
def open_google():
    browser.open('https://google.com')

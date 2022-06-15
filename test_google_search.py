from selene.support.shared import browser
from selene import be, have
import pytest


@pytest.fixture(scope='session', autouse=True)
def setup():
    browser.open('https://google.com')
    browser.driver.set_window_size(width=1920, height=1080)


def test_able_to_find_selene_in_google():
    query = browser.element('[name="q"]')
    query.should(be.blank).type('selene').press_enter()

    search = browser.element('#search')
    search.should(have.text('User-oriented Web UI browser tests in Python'))

from selene.core.condition import Condition
from selene.support.shared import browser
from selene import be, have
import pytest


selene_search_query = 'selene'
invalid_search_query = 'gfdbvnthohg'
selene_search_result = 'User-oriented Web UI browser tests in Python'


@pytest.fixture(scope='session', autouse=True)
def setup():
    browser.open('data:')
    browser.driver.set_window_size(width=1920, height=1080)


def test_able_to_find_selene_in_google():
    search_for(text=selene_search_query, condition=have.text(selene_search_result))


def test_unable_to_find_invalid_search_result_in_google():
    search_for(text=invalid_search_query, condition=have.no.texts())


def search_for(text: str, condition: Condition):
    browser.open('https://google.com')
    query = browser.element('[name="q"]')
    query.should(be.blank).type(text).press_enter()

    search = browser.element('#search')
    search.should(condition)

from selene import be, have
from selene.core.condition import Condition
from selene.support.shared import browser

selene_search_query = 'selene'
invalid_search_query = 'gfdbvnthohg'
selene_search_result = 'User-oriented Web UI browser tests in Python'


def test_able_to_find_selene_in_google(open_google):
    search(text=selene_search_query, condition=have.text(selene_search_result))


def test_unable_to_find_invalid_search_result_in_google(open_google):
    search(text=invalid_search_query, condition=have.no.texts())


def search(text: str, condition: Condition):
    query = browser.element('[name="q"]')
    query.should(be.blank).type(text).press_enter()

    browser.element('#search').should(condition)

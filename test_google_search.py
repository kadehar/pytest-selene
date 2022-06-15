from selene.support.shared import browser
from selene import be, have


def test_able_to_find_selene_in_google():
    browser.open('https://google.com')

    query = browser.element('[name="q"]')
    query.should(be.blank).type('selene').press_enter()

    search = browser.element('#search')
    search.should(have.text('User-oriented Web UI browser tests in Python'))

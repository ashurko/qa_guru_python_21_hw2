import pytest
from selene import browser, be, have

@pytest.fixture(autouse=True)
def browser_open():
   browser.open('https://duckduckgo.com/')

def test_wrong_search_duck_duck_go(browser_open):
    browser.element('[name="q"]').should(be.blank).type('[[]][[]][[]]').press_enter()
    browser.element('[class="THG_yNtlhifBrJDatoUn wZ4JdaHxSAhGy1HoNVja wN0KrcRQzChXFKiMHpCZ"]').should(have.text('ничего не найдено.'))


def test_search_duck_duck_go(browser_open):
    browser.element('[name="q"]').should(be.blank).type('привет').press_enter()
    browser.element('[class="wLL07_0Xnd1QZpzpfR4W"]').should(have.text('обращённое к кому-либо выражение дружелюбия, расположения, добрых пожеланий'))

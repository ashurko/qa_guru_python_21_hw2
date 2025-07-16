import pytest
from selene import browser

@pytest.fixture(scope= "session", autouse = True)
def browser_size():
    browser.config.window_size = (1280, 1024)
    yield
    browser.close()



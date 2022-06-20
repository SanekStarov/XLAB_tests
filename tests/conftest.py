import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def get_options():
    options = Options()
    # options.add_argument('chrome')
    options.add_argument('--start-maximized')
    # options.add_argument('--window-size=1200,980')
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    return options

@pytest.fixture
def get_web_driver(get_options):
    options = get_options
    driver = webdriver.Chrome(options=options, executable_path='/usr/local/bin/chromedriver')
    return driver

@pytest.fixture(scope='function', autouse=True)
def setup_with_close(request, get_web_driver):
    driver = get_web_driver
    url='https://test-front.onbank.online'
    if request.cls is not None:
        request.cls.driver = driver
    driver.get(url)
    yield driver
    driver.quit()

@pytest.fixture(scope='function')
def setup_without_close(get_web_driver):
    driver = get_web_driver
    url='https://test-front.onbank.online'
    # if request.cls is not None:
    #     request.cls.driver = driver
    driver.get(url)
    yield driver






import pytest

from selenium import webdriver
from pytest_bdd import given
from selenium.webdriver.chrome.service import Service

# Constants

PFIZER_PRO_URL = 'https://www.pfizerpro.com/'

# Browser setup

@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service.Service(executable_path="C:\\chromedriver_win32\\chromedriver.exe"))
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
import pytest

from selenium import webdriver
from pytest_bdd import given
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Constants

PFIZER_PRO_URL = 'https://www.pfizerpro.com/'

INCORRECT_EMAIL = "pfizerautomation@email.com"
INCORRECT_PASSWORD = '123456'

# Common Xpaths

## Login Form Modal
LoginEmail = "return document.querySelector('#iqcmfe > grv-modal > div > div.grv-modal__modal > div > grv-login-flow').shadowRoot.querySelector('grv-step-controller > grv-step > div > div.grv-login-flow-login-form > div.grv-login-flow-login-form__controls > grv-input').shadowRoot.querySelector('#email')"
LoginPassword = "return document.querySelector('#iqcmfe > grv-modal > div > div.grv-modal__modal > div > grv-login-flow').shadowRoot.querySelector('grv-step-controller > grv-step > div > div.grv-login-flow-login-form > div.grv-login-flow-login-form__controls > grv-input-password').shadowRoot.querySelector('grv-input').shadowRoot.querySelector('#password')"
LoginButton = "return document.querySelector('#iqcmfe > grv-modal > div > div.grv-modal__modal > div > grv-login-flow').shadowRoot.querySelector('grv-step-controller > grv-step > div > div.grv-login-flow-login-form > div.grv-login-flow-login-form__controls > grv-button').shadowRoot.querySelector('div > helix-button > div > span')"

## Forgot Password Modal
ForgotPasswordLink = "return document.querySelector('#iqcmfe > grv-modal > div > div.grv-modal__modal > div > grv-login-flow').shadowRoot.querySelector('grv-step-controller > grv-step > div > div.grv-login-flow-login-form > div.grv-login-flow-login-form__controls > a')"
ForgotPasswordEmail = "return document.querySelector('#iqcmfe > grv-modal > div > div.grv-modal__modal > div > grv-forgotten-password-flow').shadowRoot.querySelector('div > grv-step-controller > grv-step:nth-child(1) > grv-input').shadowRoot.querySelector('#email')"
ForgotPasswordSendButton = "return document.querySelector('#iqcmfe > grv-modal > div > div.grv-modal__modal > div > grv-forgotten-password-flow').shadowRoot.querySelector('div > grv-step-controller > grv-step:nth-child(1)').shadowRoot.querySelector('div > div > footer > grv-button').shadowRoot.querySelector('div > helix-button > div')"

# Browser setup

@pytest.fixture()
def browser():
    driver = webdriver.Chrome(service=Service(executable_path="C:\\chromedriver_win32\\chromedriver.exe"))
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

# Shared given steps

@given('I am on the PfizerPro home page')
def pp_home(browser):
    browser.get(PFIZER_PRO_URL)

@given('I click on the login link')
def pp_login(browser):
    browser.find_element(By.ID, value='i90r3u').click()
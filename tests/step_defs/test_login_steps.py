import conftest
import time

from pytest_bdd import scenarios, when, then
from selenium.webdriver.common.by import By

scenarios('../features/login.feature')

# When Steps
#TODO: refactor time.sleep to be a fixture

@when('I click the forgotten password link')
def click_forgot_password(browser):
    time.sleep(10)
    browser.execute_script(conftest.ForgotPasswordLink).click()

@when('I enter my email address')
def enter_email(browser):
    time.sleep(10)
    browser.execute_script(conftest.ForgotPasswordEmail).send_keys(conftest.INCORRECT_EMAIL)

@when('I click the request new password button')
def click_request_password(browser):
    time.sleep(5)
    browser.execute_script(conftest.ForgotPasswordSendButton).click()

@when('I enter my email and incorrect password')
def enter_incorrect_password(browser):
    time.sleep(10)
    browser.execute_script(conftest.LoginEmail).send_keys(conftest.INCORRECT_EMAIL)
    browser.execute_script(conftest.LoginPassword).send_keys(conftest.INCORRECT_PASSWORD)

@when('I enter my email and password')
def enter_credentials(browser):
    time.sleep(10)
    browser.execute_script(conftest.LoginEmail).send_keys(conftest.INCORRECT_EMAIL)
    browser.execute_script(conftest.LoginPassword).send_keys(conftest.INCORRECT_PASSWORD)

@when('I enter an incorrect email and my password')
def enter_incorrect_email(browser):
    time.sleep(10)
    browser.execute_script(conftest.LoginEmail).send_keys(conftest.INCORRECT_EMAIL)
    browser.execute_script(conftest.LoginPassword).send_keys(conftest.INCORRECT_PASSWORD)

@when('I enter an empty email and password')
def enter_empty_email(browser):
    time.sleep(10)
    browser.execute_script(conftest.LoginEmail).send_keys('')
    browser.execute_script(conftest.LoginPassword).send_keys(conftest.INCORRECT_PASSWORD)

@when('I enter a not an email address and password')
def enter_not_an_email(browser):
    time.sleep(10)
    browser.execute_script(conftest.LoginEmail).send_keys('notanemail')
    browser.execute_script(conftest.LoginPassword).send_keys(conftest.INCORRECT_PASSWORD)

@when('I click the login button')
def click_login(browser):
    browser.execute_script(conftest.LoginButton).click()

# Then Steps

# This steps should fail because currently there is no valid login
@then('I should be logged in to the application')
def logged_in(browser):
    
    assert browser.find_element(By.ID, 'logout').is_displayed()

@then('I should receive an email with a link to reset my password')
def received_email(browser):
    assert browser.find_element(By.XPATH, "//h1[contains(text(), 'Password reset')]").is_displayed()

# This steps should succeed since they are validating incorrect credentials

@then('I should see a message that my email or password is incorrect')
def incorrect_credentials(browser):
    time.sleep(10)
    assert browser.execute_script("return document.querySelector('#iqcmfe > grv-modal > div > div.grv-modal__modal > div > grv-login-flow').shadowRoot.querySelector('#invalid-login > ul > li')").is_displayed()

@then('Nothing should happen')
def nothing_happens(browser):
    time.sleep(10)
    assert browser.current_url == conftest.LOGIN_URL

#TODO: refactor log in button to be disabled
@then('The log in button will be disabled')
def login_button_disabled(browser):
    time.sleep(10)
    assert browser.execute_script(conftest.LoginButton).is_enabled()

@then ('The email field will be highlighted')
def email_field_highlighted(browser):
    time.sleep(10)
    assert browser.execute_script("return document.querySelector('#iqcmfe > grv-modal > div > div.grv-modal__modal > div > grv-login-flow').shadowRoot.querySelector('grv-step-controller > grv-step > div > div.grv-login-flow-login-form > div.grv-login-flow-login-form__controls > grv-button').shadowRoot.querySelector('div > helix-button')")
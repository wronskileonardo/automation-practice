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

@when('I enter my email and password')
def enter_credentials(browser):
    time.sleep(10)
    browser.execute_script(conftest.LoginEmail).send_keys(conftest.INCORRECT_EMAIL)
    browser.execute_script(conftest.LoginPassword).send_keys(conftest.INCORRECT_PASSWORD)

@when('I click the login button')
def click_login(browser):
    browser.execute_script(conftest.LoginButton).click()

# Then Steps

#####

# This steps should fail because currently there is no valid login
@then('I should be logged in to the application')
def logged_in(browser):
    
    assert browser.find_element(By.ID, 'logout').is_displayed()

@then('I should receive an email with a link to reset my password')
def received_email(browser):
    assert browser.find_element(By.XPATH, "//h1[contains(text(), 'Password reset')]").is_displayed()
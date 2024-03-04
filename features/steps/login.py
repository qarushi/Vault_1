import time
import os

from data.config import settings
from urllib.parse import urljoin
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from framework.webapp import webapp
from locators.path_login import ACCOUNT_ID_XPATH, PASSWORD_XPATH, USERNAME_XPATH, LOGIN_BUTTON_XPATH, ERROR_MESSAGE_XPATH
from pages.login import login
   
@given('Open the website')
def open_login_page(context):
    try:
        time.sleep(4)
        webapp.load_website()
    except:
        context.driver.close()

@when('The login portal has been opened')
def validate_login_page(context):
    try:
        time.sleep(4)
        login.validateTitle()
    except:
        webapp.get_driver().close()
        assert False, "Test is failed in validate login page title"

@then('Provide the username "{username}", account id "{account_id}" and password "{password}"')
def step_impl(context, username, account_id, password):
    try:
        time.sleep(4)
        login.enter_login_credentials(username, account_id, password)
    except Exception as e:
        raise AssertionError(f"Error while providing login details: {str(e)}")


@then('Click on the Login button')
def step_impl(context):
    try:
        webapp.click_element((By.XPATH, LOGIN_BUTTON_XPATH))
        time.sleep(3)
    except Exception as e:
        raise AssertionError(f"Error while clicking on Login button: {str(e)}")


@then('Login is successful and dashboard is opened')
def step_impl(context):
    try:
        dashboard_url = urljoin(settings['url'], "dashboard")
        WebDriverWait(webapp.get_driver(), 20).until(EC.url_matches(dashboard_url))
        time.sleep(5)
    except Exception as e:
        raise AssertionError(f"Error during successful login: {str(e)}")


@then('Dashboard Screenshot should be captured')
def step_impl(context):
    try:
        time.sleep(3)
        webapp.take_screenshot("dashboard")
    except Exception as e:
        raise AssertionError(f"Error while capturing dashboard screenshot: {str(e)}")


@then('Login is failed and invalid credential error message "{error_message}" is displayed')
def step_impl(context, error_message):
    try:
        login.validateInvalidCreds(error_message)
    except Exception as e:
        raise AssertionError(f"Error while verifying error message: {str(e)}")


@then('Screenshot of Error Message should be captured')
def step_impl(context):
    try:
        # time.sleep(2)
        webapp.take_screenshot("error_of_invalid_credentials")
    except Exception as e:
        raise AssertionError(f"Error while capturing error message screenshot: {str(e)}")
@then('Provide the account id "{account_id}" and password "{password}"')
def step_impl(context,account_id,password):
    try:
        login.enter_accountId(account_id)
        login.enter_password(password)
    except Exception as e:
        raise AssertionError(f"Error while providing account id and password: {str(e)}")
    
@then('Login is failed and empty username error is displayed')
def step_impl(context):
    try:
        login.validateEmptyUsername()
        time.sleep(2)
    except AssertionError as e:
        raise AssertionError("Empty username error message not displayed")
    except Exception as e:
        raise AssertionError(f"Error while validating empty username error: {str(e)}")


@then('Login is failed and empty password error is displayed')
def step_impl(context):
    try:
        login.validateEmptyPassword()
        time.sleep(2)
    except AssertionError as e:
        raise AssertionError("Empty password error message not displayed")
    except Exception as e:
        raise AssertionError(f"Error while validating empty password error: {str(e)}")


@then('Login is failed and empty account id error is displayed')
def step_impl(context):
    try:
        login.validateEmptyAccountId()
        time.sleep(2)
    except AssertionError as e:
        raise AssertionError("Empty account ID error message not displayed")
    except Exception as e:
        raise AssertionError(f"Error while validating empty account ID error: {str(e)}")

@then('Provide the username "{username}" and passowrd "{password}"')
def step_impl(context,username,password):
    try:
        login.enter_username(username)
        login.enter_password(password)
    except Exception as e:
        raise AssertionError(f"Error while providing username and password: {str(e)}")
@then('Provide the username "{username}" and account id "{account_id}"')
def step_impl(context,username,account_id):
    try:
        login.enter_username(username)
        login.enter_accountId(account_id)
    except Exception as e:
        raise AssertionError(f"Error while provide account id and password: {str(e)}")
    

@given('User should logged in')
def step_impl(context):
    try:
        return login.isLoggedIn()
    except Exception as e:
        raise AssertionError(f"Error while verifying login status: {str(e)}")


@then('Verify user should be able to logout')
def step_impl(context):
    try:
        time.sleep(4)
        login.logout()
    except Exception as e:
        raise AssertionError(f"Error while clicking on logout button: {str(e)}")


@then('User should be logged out successfully')
def step_impl(context):
    try:
        assert not login.isLoggedIn(), "User is still logged in"
    except Exception as e:
        raise AssertionError(f"Error while verifying logout status: {str(e)}")


@then('Take a screenshot of the landing page')
def step_impl(context):
    try:
        webapp.take_screenshot_of_current_page("login_landing_page")
    except Exception as e:
        raise AssertionError(f"Error while capturing landing page screenshot: {str(e)}")


@then(u'Close the browser')
def step_impl(context):
    try:
        webapp.get_driver().close()
    except Exception as e:
        raise AssertionError(f"Error while closing the browser: {str(e)}")

import time
import os
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('I am on the login page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)
    context.driver.get("https://vault-qa.solytics.us/login")



@when('I enter my username "{username}" and account ID "{account_id}" and password "{password}"')
def step_impl(context, username, account_id, password):
    username_field = context.driver.find_element(By.XPATH, "//input[@id='username']")
    account_id_field = context.driver.find_element(By.XPATH, "//input[@id='account_id']")
    password_field = context.driver.find_element(By.XPATH, "//input[@id='password']")

    username_field.send_keys(username)
    account_id_field.send_keys(account_id)
    password_field.send_keys(password)


@when('I click the login button')
def step_impl(context):
    login_button = context.driver.find_element(By.XPATH, "//div[@class='MuiTypography-root MuiTypography-h4 css-lv5jd5']")
    login_button.click()



@then('I should be redirected to the dashboard page')
def step_impl(context):
    WebDriverWait(context.driver, 20).until(EC.url_matches("https://vault-qa.solytics.us/dashboard"))



@then('I take a screenshot of the dashboard')
def step_impl(context):
    screenshot_path = os.path.join(os.getcwd(), "dashboard_screenshot.png")
    context.driver.save_screenshot(screenshot_path)

#Step definitions for the report feature
@when('I click on the report button')
def step_impl(context):
    report_button = WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable("//button[@title='Reports']"))
    report_button.click()



@then('I should directed to report')
def step_impl(context):
    WebDriverWait(context.driver, 20).until(EC.url_matches("https://vault-qa.solytics.us/dashboard"))



@then('I take a screenshot of the report')
def step_impl(context):
    screenshot_path = os.path.join(os.getcwd(), "report_screenshot.png")
    context.driver.save_screenshot(screenshot_path)

    context.driver.quit()




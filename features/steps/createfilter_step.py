import os
import time
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('I on the login page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.implicitly_wait(100)
    context.driver.get("https://vault-qa.solytics.us/login")

@when('I enter username "{username}" and account ID "{account_id}" and password "{password}"')
def step_impl(context, username, account_id, password):
    username_field = context.driver.find_element(By.XPATH, "//input[@id='username']")
    account_id_field = context.driver.find_element(By.XPATH, "//input[@id='account_id']")
    password_field = context.driver.find_element(By.XPATH, "//input[@id='password']")

    username_field.send_keys(username)
    account_id_field.send_keys(account_id)
    password_field.send_keys(password)


@when('I click on the login button')
def step_impl(context):
    login_button = context.driver.find_element(By.XPATH, "//div[@class='MuiTypography-root MuiTypography-h4 css-lv5jd5']")
    login_button.click()
    time.sleep(9)

@then('I should redirected to the dashboard page')
def step_impl(context):
    WebDriverWait(context.driver, 40).until(EC.url_matches("https://vault-qa.solytics.us/dashboard"))
#create filter
@when('I click on filter view button')
def step_impl(context):
    filterview_button = context.driver.find_element(By.XPATH, "//button[@title='Filter view.']")
    filterview_button.click()
    time.sleep(4)

@then('I click on add filter button')
def step_impl(context):
    addfilter_button = context.driver.find_element(By.XPATH, "//div[@class='MuiBox-root css-13fqyx2']")
    addfilter_button.click()
    time.sleep(2)
@then('I click on add filter to create new filter')
def step_impl(context):
    createfilter_button = context.driver.find_element(By.XPATH, "//button[@title='Add filter.']")
    createfilter_button.click()

@then('I click on field button')
def step_impl(context):
    field_button = context.driver.find_element(By.XPATH, "//div[contains(text(),'STATUS')]")
    field_button.click()

@then('I select the field status')
def step_impl(context):
    status_button = context.driver.find_element(By.XPATH, "//li[normalize-space()='STATUS']")
    status_button.click()

@then('I click on operator button')
def step_impl(context):
    operator_button = context.driver.find_element(By.XPATH, "//div[contains(text(),'!=')]")
    operator_button.click()

@then('I select the equal to operator')
def step_impl(context):
    equalto_button = context.driver.find_element(By.XPATH, "//li[normalize-space()='=']")
    equalto_button.click()
@then('I click on input text field')
def step_impl(context):
    textfield_button = context.driver.find_element(By.XPATH, "//input[@id='textfield']")
    textfield_button.click()

@then('I entered input Draft')
def step_impl(context):
    inputdraft_button = context.driver.find_element(By.XPATH, "//input[@id='textfield']")
    inputdraft_button.send_keys("Draft")
@then('I click on apply button')
def step_impl(context):
    apply_button = context.driver.find_element(By.XPATH, "//button[normalize-space()='Apply']")
    apply_button.click()

@then('I enter filter name')
def step_impl(context):
    filtername_button = context.driver.find_element(By.XPATH, "//input[@id=':rl:']")
    filtername_button.send_keys("Automation")
@then('I enter description')
def step_impl(context):
    description_button = context.driver.find_element(By.XPATH, "//input[@id=':rm:']")
    description_button.send_keys("Automation test")

@then('I click on save button')
def step_impl(context):
    save_button = context.driver.find_element(By.XPATH, "//button[@title='Save filter.']")
    save_button.click()
    context.driver.quit()

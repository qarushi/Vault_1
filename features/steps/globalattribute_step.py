import time
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@step('On the log in page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.implicitly_wait(40)
    context.driver.get("https://vault-qa.solytics.us/login")

@step('Enter username "{username}" and account ID "{account_id}" and password "{password}"')
def step_impl(context, username, account_id, password):
    username_field = context.driver.find_element(By.XPATH, "//input[@id='username']")
    account_id_field = context.driver.find_element(By.XPATH, "//input[@id='account_id']")
    password_field = context.driver.find_element(By.XPATH, "//input[@id='password']")

    username_field.send_keys(username)
    account_id_field.send_keys(account_id)
    password_field.send_keys(password)

@step('Click on the log in button')
def step_impl(context):
    login_button = context.driver.find_element(By.XPATH, "//div[@class='MuiTypography-root MuiTypography-h4 css-lv5jd5']")
    login_button.click()
    time.sleep(9)

@step('Redirected to the dashboard page')
def step_impl(context):
    WebDriverWait(context.driver, 40).until(EC.url_matches("https://vault-qa.solytics.us/dashboard"))

@step('I click on configuration dropdown')
def step_impl(context):
    configuration_button = context.driver.find_element(By.XPATH, "//button[@id='menu-button-Configuration']")
    configuration_button.click()

@step('I click on global attribute')
def step_impl(context):
    globalattribute_button = context.driver.find_element(By.XPATH, "//p[@title='Global Attributes']")
    globalattribute_button.click()

@step('I click on create attribute')
def step_impl(context):
    createattribute_button = context.driver.find_element(By.XPATH, "//button[@title='Create attribute.']")
    createattribute_button.click()

@step('I enter attribute name')
def step_impl(context):
    attributename_field = context.driver.find_element(By.XPATH, "//input[@name='attribute_name']")
    attributename_field.send_keys("Automation attribute")

@step('I enter attribute display name')
def step_impl(context):
    displayname_field = context.driver.find_element(By.XPATH, "//input[@name='display_name']")
    displayname_field.send_keys("Automation attribute")
    time.sleep(2)

@step('Click on entity type dropdown')
def step_impl(context):
    entitytype_dropdown = context.driver.find_element(By.XPATH, "(//div[contains(@role,'combobox')])[1]")
    entitytype_dropdown.click()


@step('I select entity type')
def step_impl(context):
    modelinventory_option = context.driver.find_element(By.XPATH, "//span[normalize-space()='ModelInventory']")
    modelinventory_option.click()

@step('I click on data type dropdown')
def step_impl(context):
    datatype_option = context.driver.find_element(By.XPATH, "(//div[normalize-space()='TEXT'])[1]")
    datatype_option.click()

@step('I select data type')
def step_impl(context):
    integer_type = context.driver.find_element(By.XPATH, "//span[text()='INTEGER']")
    integer_type.click()

@step('I click on input type dropdown')
def step_impl(context):
    inputtype_option = context.driver.find_element(By.XPATH, "(//div[contains(@role,'combobox')])[3]")
    inputtype_option.click()

@step('I select input field')
def step_impl(context):
    textfield_type = context.driver.find_element(By.XPATH, "//span[text()='TEXTFIELD']")
    textfield_type.click()

@step('I click on submit')
def step_impl(context):
    submit_button = context.driver.find_element(By.XPATH, "//button[normalize-space()='SUBMIT']")
    submit_button.click()
    context.driver.quit()

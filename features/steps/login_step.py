# import time
# import os
#
# from behave import *
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains
#
#
# @given('I am on the login page')
# def step_impl(context):
#     context.driver = webdriver.Chrome()
#     context.driver.maximize_window()
#     context.driver.get("https://vault-qa.solytics.us/login")
#     time.sleep(4)
#
#
# @when('I enter my username "{username}" and account ID "{account_id}" and password "{password}"')
# def step_impl(context, username, account_id, password):
#     username_field = context.driver.find_element(By.XPATH, "//input[@id='username']")
#     account_id_field = context.driver.find_element(By.XPATH, "//input[@id='account_id']")
#     password_field = context.driver.find_element(By.XPATH, "//input[@id='password']")
#     time.sleep(2)
#     username_field.send_keys(username)
#     account_id_field.send_keys(account_id)
#     password_field.send_keys(password)
#
#
# @When('I click the login button')
# def step_impl(context):
#     login_button = context.driver.find_element(By.XPATH,
#                                                "//div[@class='MuiTypography-root MuiTypography-h4 css-lv5jd5']")
#     login_button.click()
#     time.sleep(8)
#
#
# @then('I should be redirected to the dashboard page')
# def step_impl(context):
#     WebDriverWait(context.driver, 20).until(EC.url_matches("https://vault-qa.solytics.us/dashboard"))
#     time.sleep(4)
#
#
# # @then('I take a screenshot of the dashboard')
# # def step_impl(context):
# #     screenshot_path = os.path.join(os.getcwd(), "dashboard_screenshot.png")
# #     context.driver.save_screenshot(screenshot_path)
# #     time.sleep(3)
# #
# #
# # # @when('I enter invalid username "{username}" and account ID "{account_id}" and password "{password}"')
# # # def step_impl(context, username, account_id, password):
# # #     username_field = context.driver.find_element(By.XPATH, "//input[@id='username']")
# # #     account_id_field = context.driver.find_element(By.XPATH, "//input[@id='account_id']")
# # #     password_field = context.driver.find_element(By.XPATH, "//input[@id='password']")
# # #     time.sleep(3)
# # #     username_field.send_keys(username)
# # #     account_id_field.send_keys(account_id)
# # #     password_field.send_keys(password)
# # #     time.sleep(2)
# # #
# # #
# # # @then('I should see an error massage "{error_massage}"')
# # # def step_impl(context, error_massage):
# # #     error_massage_element = context.driver.find_element(By.XPATH, "//div[@role='alert']")
# # #     assert error_massage_element.text == error_massage
# # #     # time.sleep(2)
# # #
# # #
# # # @then('I take a screenshot of the error massage')
# # # def step_impl(context):
# # #     screenshot_path = os.path.join(os.getcwd(), "errormassages_screenshot.png")
# # #     context.driver.save_screenshot(screenshot_path)
# # #     time.sleep(4)
# # #     context.driver.quit()
# #
# # @when('I click on the report button')
# # def step_impl(context):
# #     report_button = context.driver.find_element(By.XPATH, "//button[@title='Reports']")
# #     report_button.click()
# #     time.sleep(6)
# #
# #
# # @then('I should directed to report')
# # def step_impl(context):
# #     context.driver.find_element(By.XPATH, "//*[@id='simple-tabpanel-2']/iframe")
# #     time.sleep(5)
# #
# #
# # @then('I take a screenshot of the report')
# # def step_impl(context):
# #     screenshot_path = os.path.join(os.getcwd(), "report_screenshot.png")
# #     context.driver.save_screenshot(screenshot_path)
# #     time.sleep(4)
# #
# #
# # @when('I click on the model architecture button')
# # def step_impl(context):
# #     architecture_button = context.driver.find_element(By.XPATH, "//button[@title='Models architecture.']")
# #     architecture_button.click()
# #     time.sleep(4)
# #
# #
# # @then('I should directed to model architecture page')
# # def step_impl(context):
# #     context.driver.find_element(By.XPATH, "//*[@id='simple-tabpanel-3']/div/div/div/div/div[3]/div[1]/div")
# #     time.sleep(4)
# #
# #
# # @then('I take a screenshot of the model architecture')
# # def step_impl(context):
# #     screenshot_path = os.path.join(os.getcwd(), "modelarchitecture_screenshot.png")
# #     context.driver.save_screenshot(screenshot_path)
# #     time.sleep(2)
# #
# #
# # # @when('I click on the document button')
# # # def step_impl(context):
# # #     document_button = context.driver.find_element(By.XPATH, "//button[@id='menu-button-Documents']")
# # #     document_button.click()
# # #
# # #
# # # @then('I click on the dropdown document')
# # # def step_impl(context):
# # #     dropdowndocument_button = context.driver.find_element(By.XPATH, "//li[@role='menuitem']")
# # #     dropdowndocument_button.click()
# # #     time.sleep(4)
# # #
# # #
# # # @then('I should directed to the document inventory')
# # # def step_impl(context):
# # #     WebDriverWait(context.driver, 20).until(EC.url_matches("https://vault-qa.solytics.us/document-inventory"))
# # #
# # #
# # # @then('I take a screenshot of document inventory')
# # # def step_impl(context):
# # #     screenshot_path = os.path.join(os.getcwd(), "documentinventory_screenshot.png")
# # #     context.driver.save_screenshot(screenshot_path)
#
# # @when('I click on filter view button')
# # def step_impl(context):
# #     filterview_button = context.driver.find_element(By.XPATH, "//button[@title='Filter view.']")
# #     filterview_button.click()
# #     time.sleep(3)
# # @then('I click on add filter button')
# # def step_impl(context):
# #     addfilter_button = context.driver.find_element(By.XPATH, "//div[@class='MuiBox-root css-13fqyx2']")
# #     addfilter_button.click()
# #     time.sleep(3)
# # @then('I click on add filter to create new filter')
# # def step_impl(context):
# #     createfilter_button = context.driver.find_element(By.XPATH, "//button[@title='Add filter.']")
# #     createfilter_button.click()
# #     time.sleep(1)
# # @then('I click on field button')
# # def step_impl(context):
# #     field_button = context.driver.find_element(By.XPATH, "//div[contains(text(),'STATUS')]")
# #     field_button.click()
# #     time.sleep(1)
# # @then('I select the field status')
# # def step_impl(context):
# #     status_button = context.driver.find_element(By.XPATH, "//li[normalize-space()='STATUS']")
# #     status_button.click()
# #     time.sleep(1)
# # @then('I click on operator button')
# # def step_impl(context):
# #     operator_button = context.driver.find_element(By.XPATH, "//div[contains(text(),'!=')]")
# #     operator_button.click()
# #     time.sleep(1)
# # @then('I select the equal to operator')
# # def step_impl(context):
# #     equalto_button = context.driver.find_element(By.XPATH, "//li[normalize-space()='=']")
# #     equalto_button.click()
# # @then('I click on input text field')
# # def step_impl(context):
# #     textfield_button = context.driver.find_element(By.XPATH, "//input[@id='textfield']")
# #     textfield_button.click()
# #     time.sleep(1)
# # @then('I entered input Draft')
# # def step_impl(context):
# #     inputdraft_button = context.driver.find_element(By.XPATH, "//input[@id='textfield']")
# #     inputdraft_button.send_keys("Draft")
# # @then('I click on apply button')
# # def step_impl(context):
# #     apply_button = context.driver.find_element(By.XPATH, "//button[normalize-space()='Apply']")
# #     apply_button.click()
# #     time.sleep(2)
# # @then('I enter filter name')
# # def step_impl(context):
# #     filtername_button = context.driver.find_element(By.XPATH, "//input[@id=':rl:']")
# #     filtername_button.send_keys("Automation")
# # @then('I enter description')
# # def step_impl(context):
# #     description_button = context.driver.find_element(By.XPATH, "//input[@id=':rm:']")
# #     description_button.send_keys("Automation test")
# #     time.sleep(1)
# # @then('I click on save button')
# # def step_impl(context):
# #     save_button = context.driver.find_element(By.XPATH, "//button[@title='Save filter.']")
# #     save_button.click()
# #     time.sleep(6)
# # @then('I take screenshot')
# # def step_impl(context):
# #     screenshot_path = os.path.join(os.getcwd(), "createdfilter_screenshot.png")
# #     context.driver.save_screenshot(screenshot_path)
# #     time.sleep(4)
# # @when('I hover on Automation')
# # def step_impl(context):
# #     #Find the element #need to define hover element properly
# #     element_to_hover_over = context.driver.find_element(By.XPATH, "(//div[@role='button'])[3]")
# #     #Hover the element
# #     ActionChains(context).move_to_element(element_to_hover_over).perform()
# #     time.sleep(4)
# # @then('i click on Delete')
# # def step_impl(context):
# #     delete_button = context.driver.find_element(By.XPATH, "(//*[name()='svg'][@alt='add'])[3]")
# #     delete_button.click()
#
#     context.driver.quit()
#
#
#
#
#
#
#

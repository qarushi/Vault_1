import os
import time
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


@given('log in page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.implicitly_wait(50)
    context.driver.get("https://vault-qa.solytics.us/login")


@then('I enter username "{username}" and account ID "{account_id}" and password "{password}"')
def step_impl(context, username, account_id, password):
        username_field = context.driver.find_element(By.XPATH, "//input[@id='username']")
        account_id_field = context.driver.find_element(By.XPATH, "//input[@id='account_id']")
        password_field = context.driver.find_element(By.XPATH, "//input[@id='password']")

        username_field.send_keys(username)
        account_id_field.send_keys(account_id)
        password_field.send_keys(password)


@then('i click on log in button')
def step_impl(context):
    login_button = context.driver.find_element(By.XPATH,
                                              "//div[@class='MuiTypography-root MuiTypography-h4 css-lv5jd5']")
    login_button.click()
    time.sleep(6)


#create workflow
@when('i click on the configration button')
def step_impl(context):
    configuration_button = context.driver.find_element(By.XPATH, "//button[@id='menu-button-Configuration']")
    configuration_button.click()
    time.sleep(3)


@when('i click on the regulatory guideline button')
def step_impl(context):
    guideline_button = context.driver.find_element(By.XPATH, "//p[@title='Regulatory Guidelines']")
    guideline_button.click()
    time.sleep(2)


#create new guideline
# @then('i click on create regulatory guideline button')
# def step_impl(context):
#     createguideline_button = context.driver.find_element(By.XPATH, "//button[@title='Create Regulatory Guideline']")
#     createguideline_button.click()
#
#
#
# @then('i enter regulatory guideline name')
# def step_impl(context):
#     guidelinename_field = context.driver.find_element(By.XPATH, "//input[@id=':r9:']")
#     guidelinename_field.send_keys("Automation workflow 2")
#
#
# @then('i enter regulatory guideline_description')
# def step_impl(context):
#     guidelinedescription_field = context.driver.find_element(By.XPATH, "//input[@id=':ra:']")
#     guidelinedescription_field.send_keys("Automation description")
#
#
# @then('i click on submit button')
# def step_impl(context):
#     submit_button = context.driver.find_element(By.XPATH, "//button[normalize-space()='SUBMIT']")
#     submit_button.click()
#     time.sleep(2)

#global search



@then('i click on global search bar')
def step_impl(context):
    globalsearch_field = context.driver.find_element(By.XPATH, "//input[@type='text']")
    globalsearch_field.click()
    time.sleep(3)


@then('i enter input')
def step_impl(context):
    searchbar_filed = context.driver.find_element(By.XPATH, "//input[@type='text']")
    searchbar_filed.send_keys("Automation workflow 2")
    time.sleep(2)


@then('i right click on Automation workflow 2')
def step_impl(context):
    # Wait for the element to be clickable
    workflow_element = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//td[normalize-space()='Automation workflow 2']"))
    )

    # Right click on the element
    action_chains = ActionChains(context.driver)
    action_chains.context_click(workflow_element).perform()



@then('i click on edit guideline button')
def step_impl(context):
    editguideline_button = context.driver.find_element(By.XPATH, "//span[normalize-space()='Edit regulatory guideline']")
    editguideline_button.click()
    time.sleep(2)


#first node


@then('i click on create node')
def step_impl(context):
    createnode_button = context.driver.find_element(By.XPATH, "//button[@title='Create node.']")
    createnode_button.click()


@then('i enter state name')
def step_impl(context):
    statename_filed = context.driver.find_element(By.XPATH, "//input[@type='text']")
    statename_filed.send_keys("Todo")


@then('i enter state description')
def step_impl(context):
    statedescription_filed = context.driver.find_element(By.XPATH, "//input[@name='description']")
    statedescription_filed.send_keys("automation")
    time.sleep(2)


@then('i click submit')
def step_impl(context):
    submit_button = context.driver.find_element(By.XPATH, "//button[normalize-space()='SUBMIT']")
    submit_button.click()
    time.sleep(3)


#mark as start node
@then('i click on node')
def step_impl(context):
    node_button = context.driver.find_element(By.XPATH, "//div[@title='Todo node']")
    node_button.click()
    time.sleep(1)


@then('i mark it as start node')
def step_impl(context):
    startnode_checkbox = context.driver.find_element(By.XPATH, "//div[@title='Mark as start node']//input[@name='end node']")
    startnode_checkbox.click()
    time.sleep(1)


@then('i click on delete button')
def step_impl(context):
    delete_button = context.driver.find_element(By.XPATH, "//div[@class='MuiBox-root css-1bvc4cc']//button[@type='button']")
    delete_button.click()
    time.sleep(2)


#second node
@then('I click for second node')
def step_impl(context):
    createnode_button = context.driver.find_element(By.XPATH, "//button[@title='Create node.']")
    createnode_button.click()


@then('I enter second node state')
def step_impl(context):
    statename_field = context.driver.find_element(By.XPATH, "//input[@type='text']")
    statename_field.send_keys("Development")


@then('I enter description for second node')
def step_impl(context):
    statedescription_filed = context.driver.find_element(By.XPATH, "//input[@name='description']")
    statedescription_filed.send_keys("automation description")


@then('I click on submit for second node')
def step_impl(context):
    submit_button = context.driver.find_element(By.XPATH, "//button[normalize-space()='SUBMIT']")
    submit_button.click()
    time.sleep(2)


#mark as end node
@then('I click on second node')
def step_impl(context):
    node_button = context.driver.find_element(By.XPATH, "//div[@title='Development node']")
    node_button.click()
    time.sleep(1)


@then('I mark it as end node')
def step_impl(context):
    startnode_checkbox = context.driver.find_element(By.XPATH, "//div[@title='Mark as end node']//input[@name='end node']")
    startnode_checkbox.click()
    time.sleep(1)


@then('I click on delete button for second node')
def step_impl(context):
    delete_button = context.driver.find_element(By.XPATH,
                                                    "//div[@class='MuiBox-root css-1bvc4cc']//button[@type='button']")
    delete_button.click()
    time.sleep(4)


#hover on element and connect each other
@when('i hover on first node')
def step_impl(context):
    source_element_to_hover_over = context.driver.find_element(By.XPATH, "//div[@data-id='Todo-b-source']")
    target_element_to_hover_over = context.driver.find_element(By.XPATH, "//div[@data-id='Development-b-target']")
    actions = ActionChains(context.driver)
    #time.sleep(2)
    actions.move_to_element(source_element_to_hover_over)
    time.sleep(2)
    actions.click_and_hold(source_element_to_hover_over).perform()
    time.sleep(2)

    # Move to the target element while holding the mouse button
    actions.move_to_element(target_element_to_hover_over).perform()

    # Release the mouse button on the target element
    actions.release(target_element_to_hover_over).perform()
    time.sleep(3)


@then('i compile the guideline')
def step_impl(context):
    compileguideline_button = context.driver.find_element(By.XPATH, "//button[@title='Compile regulatory guideline.']")
    compileguideline_button.click()
    time.sleep(2)
    screenshot_path = os.path.join(os.getcwd(), "guideline_screenshot.png")
    context.driver.save_screenshot(screenshot_path)

    context.driver.quit()

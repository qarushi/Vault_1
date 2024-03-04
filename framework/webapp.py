import os
import time
from selenium import webdriver
from data.config import settings
from urllib.parse import urljoin
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, ElementNotVisibleException, TimeoutException, NoSuchElementException, ElementNotInteractableException, InvalidElementStateException, InvalidSelectorException as EX


class WebApp:
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = WebApp()
        return cls.instance

    def __init__(self):
        if str(settings['browser']).lower() == "chrome":
            self.driver = webdriver.Chrome()
        else:
            self.driver = webdriver.Chrome()

    def get_driver(self):
        return self.driver

    def load_website(self):
        self.driver.get(settings['url'])

    def goto_page(self, page):
        self.driver.get(urljoin(settings['url'], page.lower()))
    def get_page_url(self,page):
        return urljoin(settings['url'],page.lower())
    def find_element(self, type, element):
        if type == "id":
            return self.driver.find_element(By.ID, element)
        elif type == "xpath":
            return self.driver.find_element(By.XPATH, element)
        elif type == "css":
            return self.driver.find_element(By.CSS_SELECTOR, element)
        else:
            return None



    def wait_and_click(self, type, element, timeout=10):
        if type in ["id", "xpath", "css"]:
            WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((getattr(By, type.upper()), element)))
            self.find_element(type, element).click()
    
    def wait_for_url_match(self, url, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.url_matches(url))
    def wait_for_element( self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
    def take_screenshot(self, name):
        # Get the current page's name
        current_page = self.driver.current_url.split('/')[-1]

        # Create the directory 'screenshots/current_page' if it doesn't exist
        screenshots_dir = os.path.join(os.getcwd(), 'screenshots', current_page)
        os.makedirs(screenshots_dir, exist_ok=True)

        # Define the screenshot path
        screenshot_path = os.path.join(screenshots_dir, f"{name}.png")

        # Take and save the screenshot
        self.driver.save_screenshot(screenshot_path)
    def click_element(self, by_locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
            self.driver.execute_script("arguments[0].click();", element)
        except EX as e:
            print("Exception! Can't click on the element")

    def input_element(self, by_locator, text):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)
        except EX as e:
            print("Exception! Can't click on the element")

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def get_title(self):
        return self.driver.title

    def get_element_attribute(self, by_locator, attribute_name):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.get_attribute(attribute_name)

    def verify_element_displayed(self, by_locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
            return element.is_displayed()
        
        except:
            return False
    def verify_component_exists(self, component):
        assert component in self.driver.find_element(By.TAG_NAME, 'body').text, \
            f"Component {component} not found on page"

webapp = WebApp.get_instance()

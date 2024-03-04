import time
from locators.path_login import ACCOUNT_ID_XPATH, ERROR_MESSAGE_XPATH, LOGOUT_BUTTON, PASSWORD_XPATH, USERNAME_XPATH,USERNAME_REQUIRED_ERROR_XPATH,ACCOUNT_ID_REQUIRED_ERROR_XPATH,PASSWORD_REQUIRED_ERROR_XPATH
from framework.webapp import webapp
from selenium.webdriver.common.by import By

class Login():
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = Login()
        return cls.instance

    def __init__(self):
        self.driver = webapp.get_driver()
        self.REQUIRED = "Required"
    
    def isLoggedIn(self):
        time.sleep(5)
        current_url = self.driver.current_url
        return 'dashboard' in current_url


    def enter_login_credentials(self, username,account_id,password):
        time.sleep(2)
        webapp.input_element((By.XPATH,USERNAME_XPATH),username)
        webapp.input_element((By.XPATH,ACCOUNT_ID_XPATH),account_id)
        webapp.input_element((By.XPATH,PASSWORD_XPATH),password)
    
    def enter_username(self , username):
        webapp.input_element((By.XPATH,USERNAME_XPATH),username)

    def enter_accountId(self, account_id):
        webapp.input_element((By.XPATH,ACCOUNT_ID_XPATH),account_id)
    
    def enter_password(self, password):
        webapp.input_element((By.XPATH,PASSWORD_XPATH),password)

    def validateInvalidCreds(self,error_message):
        # time.sleep(2)
        error_message_element = webapp.get_element_text((By.XPATH, ERROR_MESSAGE_XPATH))
        assert error_message_element == error_message, f"Expected error message: {error_message}, Actual error message: {error_message_element}"
    def validateEmptyUsername(self):
        assert webapp.get_element_text((By.XPATH,USERNAME_REQUIRED_ERROR_XPATH))== self.REQUIRED

    def validateEmptyPassword(self):
        assert webapp.get_element_text(( By.XPATH,PASSWORD_REQUIRED_ERROR_XPATH))== self.REQUIRED
    
    def validateEmptyAccountId(self):
        assert webapp.get_element_text((By.XPATH,ACCOUNT_ID_REQUIRED_ERROR_XPATH))== self.REQUIRED
    def validateTitle(self):
        assert webapp.get_title() == "MRM Vault"
    def logout(self):
        # # Use the existing webapp methods to find and click the logout button
        # webapp.click_on("xpath", "//button[@title='Logout']//*[name()='svg']")
        webapp.click_element((By.XPATH,LOGOUT_BUTTON))


    
login = Login.get_instance()

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.Login_Page import Login_Page_Class


class Registration_Page_Class(Login_Page_Class):

    text_name_xpath = "//input[@id='name']"
    text_confirm_password_xpath = "//input[@id='password-confirm']"


    def Enter_Name(self, name):
        self.driver.find_element(By.XPATH, self.text_name_xpath).send_keys(name)

    def Enter_Confirm_Password(self, password):
        self.driver.find_element(By.XPATH, self.text_confirm_password_xpath).send_keys(password)




# How to create  bat file
# Jenkins and git
# Go to github and register and login
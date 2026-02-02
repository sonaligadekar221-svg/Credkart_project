from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Login_Page_Class:
    text_email_id = "email"
    text_password_id = "password"
    click_login_register_button_Xpath = "//button[@type='submit']"
    click_menu_button_Xpath = "//a[@role='button']"
    click_logout_button_Xpath = "//a[normalize-space()='Logout']"

    def __init__(self, driver):
        self.driver = driver

    def Enter_Email(self, email):
        self.driver.find_element(By.ID, self.text_email_id).send_keys(email)

    def Enter_Password(self, password):
        self.driver.find_element(By.ID, self.text_password_id).send_keys(password)

    def Click_Login_Register_Button(self):
        self.driver.find_element(By.XPATH, self.click_login_register_button_Xpath).click()

    def Click_Menu_button(self):
        self.driver.find_element(By.XPATH, self.click_menu_button_Xpath).click()

    def Click_Logout_button(self):
        self.driver.find_element(By.XPATH, self.click_logout_button_Xpath).click()

    def verify_menu_button_visibility(self):
        try:
            wait = WebDriverWait(self.driver, 5)
            wait.until(expected_conditions.visibility_of_element_located((By.XPATH,  self.click_menu_button_Xpath)))
            self.driver.find_element(By.XPATH, self.click_menu_button_Xpath)
            return "pass"
        except:
            return "fail"
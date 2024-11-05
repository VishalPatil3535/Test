from selenium.webdriver.common.by import By
class Login_elements:
    Login_link_xpath = "//a[@id='login-or-signup']"
    Email_textbox_xpath = "//input[@id='username-field']"
    Password_textbox_xpath = "//input[@id='current-password-field']"
    Login_button_xpath = "//button[@type='submit']"
    switch_frame_xpath = "//iframe[@name='__uspapiLocator']"
    error_msg = "//div[.='Your login or password is incorrect.']"

    def __init__(self,driver):
        self.driver = driver

    def click_login_link(self):
        self.driver.find_element(By.XPATH,self.Login_link_xpath).click()

    def enter_email(self,email):
        self.driver.find_element(By.XPATH, self.Email_textbox_xpath).clear()
        self.driver.find_element(By.XPATH, self.Email_textbox_xpath).send_keys(email)

    def enter_password(self,password):
        self.driver.find_element(By.XPATH, self.Password_textbox_xpath).clear()
        self.driver.find_element(By.XPATH, self.Password_textbox_xpath).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(By.XPATH,self.Login_button_xpath).click()

    def enter_invalid_email(self,invalid_email):
        self.driver.find_element(By.XPATH, self.Email_textbox_xpath).clear()
        self.driver.find_element(By.XPATH, self.Email_textbox_xpath).send_keys(invalid_email)

    def error_msg1(self):
        msg = self.driver.find_element(By.XPATH,self.error_msg).text
        return msg

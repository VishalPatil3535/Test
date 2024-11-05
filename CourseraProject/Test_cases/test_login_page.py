import logging
import time

from selenium import webdriver

from Utilities.read_properties import read_config
from Page_object_Base_pages.Login_page import Login_elements
from Utilities.custom_logger import log_maker


class Test_01_Login:
    base_url = read_config.get_login_url()
    email = read_config.get_login_username()
    password = read_config.get_login_password()
    invalid_email = read_config.get_login_invalid_username()
    error_msg = read_config.get_error_msg()
    logging = log_maker.log_gen()


    def test_title_check(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.base_url)
        title = self.driver.title
        acp_title = "Khan Academy | Free Online Courses, Lessons & Practice"
        self.logging.info("***************Test the page title**************")
        if title == acp_title:
            assert True
            self.driver.close()
        else:
            self.driver.close()
            assert False

    def test_enter_valid_email(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get(self.base_url)
        self.lp = Login_elements(self.driver)
        self.lp.click_login_link()
        self.lp.enter_email(self.email)
        self.lp.enter_password(self.password)
        self.lp.click_login_button()
        lg_title = self.driver.title
        print(lg_title)
        self.logging.debug("***************debug**************")
        act_title = "Khan Academy"
        if lg_title == act_title:
            assert True
            self.driver.close()
        else:
            self.driver.close()
            assert False

    def test_enter_invalid_email(self):
        try:
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()
            self.driver.implicitly_wait(5)
            self.driver.get(self.base_url)
            self.lp = Login_elements(self.driver)
            self.lp.click_login_link()
            self.lp.enter_invalid_email(self.invalid_email)
            self.lp.enter_password(self.password)
            self.lp.click_login_button()
            self.logging.critical("***************critical**************")
        except Exception as e:
            raise ValueError (f"Your login or password is incorrect.{str(e)}")
        finally:
            self.driver.close()
            print("closed")

    def test_enter_invalid1_email(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get(self.base_url)
        self.lp = Login_elements(self.driver)
        self.lp.click_login_link()
        self.lp.enter_invalid_email(self.invalid_email)
        self.lp.enter_password(self.password)
        self.lp.click_login_button()
        self.logging.error("***************error**************")
        msg = self.lp.error_msg1()
        uu = self.error_msg
        if msg == uu:
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\test_screenshots.png")
            self.driver.close()
            assert False


        self.logging.warning("************warning***********")
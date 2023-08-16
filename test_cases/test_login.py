import time

from pageObjects.LoginPage import LoginPage
from selenium import webdriver
import pytest


class TestsLogin:
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    username = "Admin"
    password = "admin123"
    wrngpswrd = "admin"

    def test_loginpage(self,setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.url)
        self.driver.implicitly_wait(10)
        self.lp=LoginPage(self.driver)
        self.lp.userName(self.username)
        self.lp.passWord(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        actual_title=self.driver.title

        if actual_title == "OrangeHRM":
            assert True
        else:
            assert False
        self.driver.close()

    def test_loginfailure(self,setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.implicitly_wait(10)
        self.lp=LoginPage(self.driver)
        self.lp.userName(self.username)
        self.lp.passWord(self.wrngpswrd)
        self.lp.clickLogin()
        time.sleep(5)
        self.lp.geterrormsg()
        self.driver.close()





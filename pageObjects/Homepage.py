import time

from TestData import data
from TestLocators import locators
from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def Click_PIM(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element(by=By.LINK_TEXT, value=locators.Locators().PIM_Link).click()


    def Add_Employee(self, firstName, lastname):
        self.driver.implicitly_wait(10)
        self.driver.find_element(by=By.XPATH, value=locators.Locators().Add_button).click()
        self.driver.find_element(by=By.NAME, value=locators.Locators().First_name).send_keys(
            firstName)
        self.driver.find_element(by=By.NAME, value=locators.Locators().Last_name).send_keys(
            lastname)
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value=locators.Locators().Save_Button).click()
        time.sleep(5)

    def Edit_Employee(self,employeeName, lastName):
        time.sleep(10)
        self.driver.implicitly_wait(10)
        self.driver.find_element(by=By.LINK_TEXT, value=locators.Locators().PIM_Link).click()
        self.driver.find_element(by=By.XPATH, value=locators.Locators().Employee_name).send_keys(
            employeeName)
        self.driver.find_element(by=By.XPATH, value=locators.Locators().Search_Button).click()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=locators.Locators().Edit_Employee).click()
        time.sleep(5)
        self.driver.find_element(by=By.NAME, value=locators.Locators().Last_name).send_keys(
            lastName)
        self.driver.find_element(by=By.XPATH, value=locators.Locators().Edit_SaveBtn).click()
        time.sleep(5)

    def Delete_Employee(self, employeeName):
        self.driver.implicitly_wait(10)
        self.driver.find_element(by=By.LINK_TEXT, value=locators.Locators().PIM_Link).click()
        self.driver.find_element(by=By.XPATH, value=locators.Locators().Employee_name).send_keys(
            employeeName)
        self.driver.find_element(by=By.XPATH, value=locators.Locators().Search_Button).click()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=locators.Locators().Delete_Employee).click()
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value=locators.Locators().DelConfirm_Popup).click()
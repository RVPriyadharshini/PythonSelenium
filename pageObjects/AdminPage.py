import time
import traceback
from TestLocators import locators
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class AdminPage:
    def __init__(self, driver):
        self.driver = driver

    def ResetPassword(self, username):
     try:
        self.driver.implicitly_wait(10)
        self.driver.find_element(by=By.XPATH, value=locators.Locators().Forget_PasswordLink).click()
        time.sleep(3)
        self.driver.find_element(by=By.NAME, value=locators.Locators().username_input_box).send_keys(
            username)
        self.TakeScreenshot("ResetImage")
        self.driver.find_element(by=By.XPATH, value=locators.Locators().Reset_password).click()

     except  NoSuchElementException as e:
        error_message = str(e)
        stack_trace = str(traceback.format_exc())
        print(error_message)
        print(stack_trace)


    def TakeScreenshot(self, ImageName):
        self.driver.get_screenshot_as_file("Screenshot/Screenshot_Clipping/" + ImageName + ".png")

    def GettitleName(self):
        time.sleep(5)
        actual_title = self.driver.title

        if actual_title == "OrangeHRM":
            assert True
        else:
            assert False
    def assertValidation(self, extractmsg, inputmsg):
        if extractmsg == inputmsg:
            assert True
            print(extractmsg)
        else:
            assert False



    def HeaderChecking(self):
        time.sleep(3)

        self.driver.find_element(by=By.LINK_TEXT, value=locators.Locators().Admin_Link).click()
        time.sleep(3)
        user_man = self.driver.find_element(by=By.XPATH, value=locators.Locators().User_Management).text
        self.assertValidation(user_man, "User Management")

        job = self.driver.find_element(by=By.XPATH, value=locators.Locators().Job_Header).text
        self.assertValidation(job, "Job")

        organization = self.driver.find_element(by=By.XPATH, value=locators.Locators().Organization_Header).text
        self.assertValidation(organization, "Organization")

        qualification = self.driver.find_element(by=By.XPATH, value=locators.Locators().Qualification_Header).text
        self.assertValidation(qualification, "Qualifications")

        nationalities = self.driver.find_element(by=By.LINK_TEXT, value=locators.Locators().Nationalities_Header).text
        self.assertValidation(nationalities, "Nationalities")

        branding = self.driver.find_element(by=By.LINK_TEXT, value=locators.Locators().Corporate_Branding_Header).text
        self.assertValidation(branding, "Corporate Branding")

        configuration = self.driver.find_element(by=By.XPATH, value=locators.Locators().Configuration_Header).text
        self.assertValidation(configuration, "Configuration")







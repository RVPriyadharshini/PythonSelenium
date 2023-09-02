import time
from pageObjects.AdminPage import AdminPage
from TestData.data import Data
from pageObjects.LoginPage import LoginPage




class TestsAdminHeaderValidation:

    #Test to validate the Admin Tabs are displaying properly
    def test_AdminHeaderValidation(self, setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(Data.url)
        self.driver.implicitly_wait(10)
        time.sleep(5)
        self.lp = LoginPage(self.driver)
        self.lp.userName(Data.username)
        self.lp.passWord(Data.password)
        time.sleep(3)
        self.lp.clickLogin()
        time.sleep(3)
        self.ah = AdminPage(self.driver)
        self.ah.GettitleName()
        self.ah.HeaderChecking()
        self.driver.close()




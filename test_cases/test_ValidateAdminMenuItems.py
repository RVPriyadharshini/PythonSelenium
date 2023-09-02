import time
from pageObjects.AdminPage import AdminPage
from TestData.data import Data
from pageObjects.LoginPage import LoginPage


class TestsAdminMenualidation:

    #Test to validate the Admin Menu left panel sides are displaying properly
    def test_AdminMenuValidation(self, setup):
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
        self.ah.MenuChecking()
        self.driver.close()





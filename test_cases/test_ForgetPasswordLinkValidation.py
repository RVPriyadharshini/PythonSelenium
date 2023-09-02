import time
from pageObjects.AdminPage import AdminPage
from TestData.data import Data


class TestsForgetPasswordLinkValidation:

    def test_ForgetPasswordLinkValidation(self, setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(Data.url)
        self.driver.implicitly_wait(10)
        time.sleep(5)
        self.ts = AdminPage(self.driver)
        self.ts.ResetPassword(Data.username)
        self.driver.close()






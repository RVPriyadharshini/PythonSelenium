import time
from pageObjects.AdminPage import AdminPage


class TestsForgetPasswordLinkValidation:
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    username = "Admin"

    def test_ForgetPasswordLinkValidation(self, setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.url)
        self.driver.implicitly_wait(10)
        time.sleep(5)
        self.ts = AdminPage(self.driver)
        self.ts.ResetPassword(self.username)
        # self.ts.GettitleName()
        # self.ts.HeaderChecking()





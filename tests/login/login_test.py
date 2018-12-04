from pages.Login.login_page import LoginPage
from utilities.result_status import ResultStatus
import unittest
import pytest


@pytest.mark.usefixture("oneTimeSetUp", "setUp")
class LoginTest(unittest.TestCase):

    @pytest.fixture(autouse=2)
    def objectSetup(self, oneTimeSetUp):
        self.lg = LoginPage(self.driver)
        self.test_status = ResultStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_verifyLoginSuccessful(self):
        self.lg.login("000165694001", "1", "2", "3", "4")
        result_success = self.lg.verifyLoginSuccessful()
        self.test_status.markFinal("Test Login Successful", result_success, "Login successfully")

    @pytest.mark.run(order=2)
    def test_verifyLoginFail(self):
        self.lg.logOut()
        self.lg.login("0356940090", "1", "2", "3", "4")
        result_fail = self.lg.verifyLoginFailed()
        self.test_status.markFinal(" Test Login Failed", result_fail, "Login Failed")



import utilities.custom_logger as cl
import logging
from base.basepage import BasePage


class LoginPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locator
    _login_button = ".btn-login.d-lg-block"
    _phone_number_field = ".input-wrapper [type]"
    _next_button = "[class='btn btn-type-2 ']"
    _otp_field_1 = "[data-id='0']"
    _otp_field_2 = "[data-id='1']"
    _otp_field_3 = "[data-id='2']"
    _otp_field_4 = "[data-id='3']"
    _user_setting_icon = "//div[@id='root']//div[3]"
    _log_out_button = ".btn-logout"

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="css")

    def enterPhoneNumber(self, phone_number):
        self.sendKeys(phone_number, self._phone_number_field, locatorType="css")

    def clickNextButton(self):
        self.elementClick(self._next_button, locatorType="css")

    def enterOTP1(self, otp):
        self.sendKeys(otp, self._otp_field_1, locatorType="css")

    def enterOTP2(self, otp):
        self.sendKeys(otp, self._otp_field_2, locatorType="css")

    def enterOTP3(self, otp):
        self.sendKeys(otp, self._otp_field_3, locatorType="css")

    def enterOTP4(self, otp4):
        self.sendKeys(otp4, self._otp_field_4, locatorType="css")

    def login(self, phone, otp, otp2, otp3, otp4):
        self.clickLoginButton()
        self.wait(5)
        self.enterPhoneNumber(phone)
        self.wait(5)
        self.clickNextButton()
        self.wait(5)
        self.enterOTP1(otp)
        self.enterOTP2(otp2)
        self.enterOTP3(otp3)
        self.enterOTP4(otp4)
        self.wait(5)

    def verifyLoginSuccessful(self):
        result = self.isElementPresent(self._user_setting_icon, locatorType="xpath")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent(".Toastify__toast-container--top-right", locatorType="css")
        return result

    def clearFields(self):
        phone_number = self.getElement(locator=self._phone_number_field)
        phone_number.clear()

    def logOut(self):
        self.elementClick(self._user_setting_icon, locatorType="xpath")
        self.elementClick(self._log_out_button, locatorType="css")




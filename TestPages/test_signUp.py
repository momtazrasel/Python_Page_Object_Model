from Pages.BasePage import BaseClass
from Pages.SignUpPage import SignUpPage


class SignUpTest(BaseClass):
    def test_sign_up(self):
        test = SignUpPage(self.driver)
        test.sign_up()

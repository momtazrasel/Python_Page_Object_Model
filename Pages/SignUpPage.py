from Locators.DemoBlazeLocators import SignUpLocator
from Pages.HomePage import HomePage


class SignUpPage(HomePage):
    def __init__(self, driver):
        self.driver = driver
        self.locator = SignUpLocator()

    def sign_up(self):
        self.verify_signup_button_text("Sign up", *self.locator.signUpTab)
        self.click_element(*self.locator.signUpTab)
        # self.assert_text_present("Sign Up", *self.locator.signUpTab)


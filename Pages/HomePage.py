
class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def click_element(self, *locator):
        self.driver.find_element(*locator).click()

    def verify_signup_button_text(self, expected_text, *locator):
        actual_txt = self.driver.find_element(*locator).text
        assert actual_txt == expected_text, \
            f"Expected '{expected_text}' but found '{actual_txt}' for signup button text."

    def send_keys(self, *locator, keys):
        self.driver.find_element(*locator).send_keys(keys)



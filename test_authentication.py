import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

class TestAuthentication(unittest.TestCase):

    def setUp(self):
        # Setup WebDriver (change path if needed)
        self.driver = webdriver.Chrome(executable_path="path_to_chromedriver")
        self.driver.maximize_window()

    def test_sign_up_success(self):
        driver = self.driver
        driver.get("https://your-web-application-url.com/signup")
        
        # Fill in the Sign Up form
        driver.find_element(By.ID, "email").send_keys("testuser@example.com")
        driver.find_element(By.ID, "password").send_keys("Password123")
        driver.find_element(By.ID, "confirm_password").send_keys("Password123")
        
        # Click the Sign Up button
        driver.find_element(By.ID, "sign_up_button").click()
        
        # Assert success message
        success_message = driver.find_element(By.ID, "sign_up_success_message").text
        self.assertEqual(success_message, "Account created successfully")
        
    def test_sign_up_failure_empty_fields(self):
        driver = self.driver
        driver.get("https://your-web-application-url.com/signup")
        
        # Click Sign Up without filling in any details
        driver.find_element(By.ID, "sign_up_button").click()
        
        # Assert that error message appears for empty fields
        error_message = driver.find_element(By.ID, "error_message").text
        self.assertIn("Please fill in all fields", error_message)
        
    def test_sign_up_failure_password_mismatch(self):
        driver = self.driver
        driver.get("https://your-web-application-url.com/signup")
        
        # Fill in Sign Up form with mismatched passwords
        driver.find_element(By.ID, "email").send_keys("testuser@example.com")
        driver.find_element(By.ID, "password").send_keys("Password123")
        driver.find_element(By.ID, "confirm_password").send_keys("Password321")
        
        # Click Sign Up button
        driver.find_element(By.ID, "sign_up_button").click()
        
        # Assert error message for password mismatch
        error_message = driver.find_element(By.ID, "error_message").text
        self.assertIn("Passwords do not match", error_message)

    def test_sign_in_success(self):
        driver = self.driver
        driver.get("https://your-web-application-url.com/signin")
        
        # Fill in Sign In form
        driver.find_element(By.ID, "email").send_keys("testuser@example.com")
        driver.find_element(By.ID, "password").send_keys("Password123")
        
        # Click Sign In button
        driver.find_element(By.ID, "sign_in_button").click()
        
        # Assert login success (e.g., checking the presence of a logout button)
        logout_button = driver.find_element(By.ID, "logout_button")
        self.assertTrue(logout_button.is_displayed())

    def test_sign_in_failure_invalid_credentials(self):
        driver = self.driver
        driver.get("https://your-web-application-url.com/signin")
        
        # Fill in invalid credentials
        driver.find_element(By.ID, "email").send_keys("wronguser@example.com")
        driver.find_element(By.ID, "password").send_keys("WrongPassword")
        
        # Click Sign In button
        driver.find_element(By.ID, "sign_in_button").click()
        
        # Assert error message for invalid credentials
        error_message = driver.find_element(By.ID, "error_message").text
        self.assertIn("Invalid credentials", error_message)

    def test_sign_in_failure_empty_fields(self):
        driver = self.driver
        driver.get("https://your-web-application-url.com/signin")
        
        # Click Sign In without filling in any details
        driver.find_element(By.ID, "sign_in_button").click()
        
        # Assert error message for empty fields
        error_message = driver.find_element(By.ID, "error_message").text
        self.assertIn("Please fill in all fields", error_message)
        
    def test_sign_out(self):
        driver = self.driver
        driver.get("https://your-web-application-url.com/signin")
        
        # Log in first
        driver.find_element(By.ID, "email").send_keys("testuser@example.com")
        driver.find_element(By.ID, "password").send_keys("Password123")
        driver.find_element(By.ID, "sign_in_button").click()
        
        # Click on Sign Out
        driver.find_element(By.ID, "sign_out_button").click()
        
        # Assert user is redirected to login page
        login_page_url = "https://your-web-application-url.com/signin"
        self.assertEqual(driver.current_url, login_page_url)

    def tearDown(self):
        # Close the browser after tests
        time.sleep(2)  # Adding delay before closing for any final checks
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
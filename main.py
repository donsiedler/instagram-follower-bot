import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

IG_USERNAME = os.environ.get("IG_USERNAME")
IG_PASSWORD = os.environ.get("IG_PASSWORD")
ACCOUNT_NAME = "natgeotravel"


class InstaFollower:
    def __init__(self, options, service):
        self.driver = webdriver.Chrome(service=service, options=chrome_options)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")

        # Allow essential cookies
        cookies_btn = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div["
                                                         "2]/div/div/div/div/div[2]/div/button[1]")
        cookies_btn.click()

        time.sleep(2)

        # Locate login inputs and button
        username_input = self.driver.find_element(By.NAME, "username")
        password_input = self.driver.find_element(By.NAME, "password")
        login_btn = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[1]/div/div/div/div["
                                                       "1]/section/main/div/div/div[1]/div[2]/form/div/div[3]/button")

        username_input.send_keys(IG_USERNAME)
        password_input.send_keys(IG_PASSWORD)
        login_btn.click()

        time.sleep(4)

        # Handle 'Save Your Login Info' prompt
        not_now_btn = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div["
                                                         "1]/div[2]/section/main/div/div/div/div/button")
        not_now_btn.click()

        time.sleep(2)

        # Disable notifications
        disable_btn = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div["
                                                         "2]/div/div/div/div/div[2]/div/div/div[3]/button[2]")
        disable_btn.click()

    def find_followers(self):
        pass

    def follow(self):
        pass


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)  # Keeps the browser open!
chrome_options.add_argument("--start-maximized")
service = Service(ChromeDriverManager().install())

bot = InstaFollower(options=chrome_options, service=service)
bot.login()
bot.find_followers()
bot.follow()

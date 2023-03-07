import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

IG_USERNAME = os.environ.get("IG_USERNAME")
IG_PASSWORD = os.environ.get("IG_PASSWORD")
ACCOUNT_NAME = "natgeotravel"


class InstaFollower:
    def __init__(self, options, service):
        self.driver = webdriver.Chrome(service=service, options=chrome_options)

    def login(self):
        self.driver.get("https://www.instagram.com/")

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

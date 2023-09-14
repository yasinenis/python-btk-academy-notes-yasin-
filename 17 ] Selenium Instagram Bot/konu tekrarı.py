from instaUserinfo import email, password
from selenium import webdriver

class Instagram:
    def __init__(self, email, password):
        self.browser = webdriver.Chrome()
        self.email = email
        self.password = password 

    def signIn(self):
        self.browser.get("https://www.instagram.com/")
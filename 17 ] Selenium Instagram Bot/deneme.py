from instaUserinfo import email, password
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

class Instagram:
    def __init__(self, email, password):
        self.browser = webdriver.Chrome()   # driver oluşturduk
        self.email = email
        self.password = password

    def signIn(self):
        self.browser.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)
        emailInput = self.browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[1]/div/label/input")
        passwordInput = self.browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[2]/div/label/input")

        # sifre ve email girilsin
        emailInput.send_keys(self.email)
        passwordInput.send_keys(self.password)
        # imlec password kısmındayken enter tusuna basalım
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(3)


    def getFollowers(self):
        self.browser.get("https://www.instagram.com/hesapadi")
        time.sleep(2)
        
        tikla = self.browser.find_element(By.CSS_SELECTOR, ".x1i10hfl.xjbqb8w.x6umtig.x1b1mbwd.xaqea5y.xav7gou.x9f619.x1ypdohk.xt0psk2.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz._alvs._a6hd").click()
        time.sleep(2)

        # scrol aşağı indir.










insta = Instagram(email, password)

insta.signIn()
insta.getFollowers()
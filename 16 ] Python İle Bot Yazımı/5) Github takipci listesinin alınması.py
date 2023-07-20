# NOT ÇALIŞTIRILMADAN ÖNCE KÜTÜPHANESİ İLE AYNI DİZİNDE OLMASI GEREKEBİLİR

from githublib import username, password
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Github:
    def __init__(self, username, password):
        self.browser = webdriver.Chrome()
        self.username = username 
        self.password = password
        self.followers = []


    def signIn(self):
        self.browser.get("https://github.com/login")
        time.sleep(2)

        username_input = self.browser.find_element(By.CSS_SELECTOR, '.form-control.input-block.js-login-field')
        username_input.send_keys(self.username)

        time.sleep(2)

        password_input = self.browser.find_element(By.ID, 'password').send_keys(self.password)

        time.sleep(2)

        sign_in_button = self.browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary.btn-block.js-sign-in-button')
        sign_in_button.click()



    def getFollowers(self):
        self.browser.get("https://github.com/sylveon?tab=followers")
        time.sleep(2)

        items = self.browser.find_elements(By.CSS_SELECTOR, '.d-table.table-fixed.col-12.width-full.py-4.border-bottom.color-border-muted')
        for i in items:
            self.followers.append(i.find_element(By.CSS_SELECTOR, '.f4.Link--primary').text)
            
        while True:
            links = self.browser.find_element(By.CLASS_NAME, 'pagination').find_elements(By.TAG_NAME, 'a')

            if len(links) == 1:
                if links[0].text == "Next":
                    links[0].click()
                    time.sleep(1)
                    print("bir sonraki sayfaya geçiliyor")
                          
                    items = self.browser.find_elements(By.CSS_SELECTOR, '.d-table.table-fixed.col-12.width-full.py-4.border-bottom.color-border-muted')
                    for i in items:
                        self.followers.append(i.find_element(By.CSS_SELECTOR, '.f4.Link--primary').text)
                else:
                    break
            else:
                for link in links:
                    if link.text == "Next":
                        link.click()
                        time.sleep(1)
                        items = self.browser.find_elements(By.CSS_SELECTOR, '.d-table.table-fixed.col-12.width-full.py-4.border-bottom.color-border-muted')
                        for i in items:
                            self.followers.append(i.find_element(By.CSS_SELECTOR, '.f4.Link--primary').text)
                    else:
                        continue

github = Github(username, password)

github.getFollowers()

print(len(github.followers))
print(github.followers)
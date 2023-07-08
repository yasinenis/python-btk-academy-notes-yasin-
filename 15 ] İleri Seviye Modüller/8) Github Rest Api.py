api = "api.github.com"

api = "api.github.com/users/sadikturan"  
#kullanıcı bilgilerinin json olarak getirir

api = "api.github.com/users/sadikturan/repos" 
# ilgili kullanıcının repolarını getirir 

# mesela bir repo yaratmaya çalışsak bunun için token yontemini kullanabiliriz çünkü sadece sahibi repo oluşturabilir.
# githubda önceden oluşturduğumuz şifreli tokeni kullanmamız gerek işlemlerimizde ki github sitesi anlasınki sahibi olarak bu işlemi yapıyoruz.


#-------------------ÜST KISIM SADECE ÖN BİLGİ İÇİN------------------------

import requests
import json

class Github:
    def __init__(self):
        self.api_url = 'https://api.github.com' # temel api adresi
        self.token = 'token buraya yazılacak'

    def getUser(self, username):
        response = requests.get(self.api_url+"/users/"+ username)
        # gelecek olan response üzerinde belli bilgilere ulaşabilmek için bunu json stringi, dict bilgiye çevirmeliyiz
        return response.json() # response.loads() metodunu kullanmak yerine yapılabilir.

    def getRepositories(self, username):
        response = requests.get(self.api_url+'/users/'+ username+'/repos')
        return response.json()

    def createRepository(self, name):
        response = requests.post(
            self.api_url+'/user/repos',
            headers={'Authorization': 'Token ' + self.token},
            json={
            "name": name,
            "description": "This is your first repository",
            "homepage": "https://github.com",
            "private": False,
            "has_issues": True,
            "has_projects": True,
            "has_wiki": True
        })
        return response.json()



github = Github()


while True:
    secim = input("1- Find User\n2- Get Repositories\n3- Create Repository\n4- Exit\nSeçim: ")

    if secim == "4":
        break
    else:
        if secim == "1":
            username = input('username: ')
            result = github.getUser(username)
            print(f"\n\nname: {result['name']} \npublic repos: {result['public_repos']} \nfollower: {result['followers']}\n   ---")


        elif secim == "2":
            username = input('username: ')
            result = github.getRepositories(username)
            for repo in result:
                print(repo['name'])

        elif secim == "3":
            name = input('repository name: ')
            result = github.createRepository(name)
            print(result)
        else:
            print("yanlış bir seçim yaptınız.")
# json uygulaması yapıyoruz

import json
import os   # user listesini okuyacağımız zaman önce dosyanın olup olmadığını kontrol edecek

class User:     # kullanıcı oluşturmak istediğimizde user classını tanımlıycaz.
                # user classı içinde kullanıcı parola mail bilgileri olacak.
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

class UserRepository:   # user classını yönetecek (örnek kullanıcı oluşturma gibi işlemler fonskiyonlar burda olcak)
    def __init__(self):
        self.users = []     # kullanıcı listesi yaptık
        self.isLoggedIn = False  # varsayılan olarak kullanıcı login olmamıs ayarlı
        self.currentUser = {}   # login olan kullanıcımım user objesini buna atcaz (login olmuş anlamında ve bilgilere ulaşılabilir)

        # load users from .json file
        self.loadUsers()     # bunun fonksiyonunu aşağıda oluşturduk

    def loadUsers(self): # user listesine dosyadan tüm bilgileri alacak
        if os.path.exists('15 ] İleri Seviye Modüller/users.json'):   # dosya okumadan önce okunacak dosyanın olup olmadığını kontrol etmek
            # yukarıdan true minvalinde bir sonuc geliyosa dosya var demektir (os.exist metodu) ve aşağıdaki işleme geçilir
            with open('15 ] İleri Seviye Modüller/users.json','r', encoding="utf-8") as file:
                users = json.load(file) # dosyadan okuma işlemi (load() metodu ile)
                for user in users:
                    user = json.loads(user) # json stringi olarak berbat görüntü olduğu için ve json stringi halde aradam istediğimiz bilgiyi cımbızlayamadığımız için jsonstringi ifadeyi dict e çevirmiş olduk 
                    newUser = User(username = user['username'], password = user['password'], email = user['email'])
                    self.users.append(newUser)
            print('Bilgi Ekranı'.center(50,'-'))
            print(self.users)


    def register(self, user: User): # gelen user bilgisinin tipi user olmalı dedik ( user: User)
        self.users.append(user)
        self.savetoFile()
        print('Bilgi Ekranı'.center(50,'-'))
        print('kullanıcı oluşturuldu.')

    def login(self, username, password):
        
        for user in self.users: # users objeleri üzerinde tek tek dolaşıcak
            if user.username == username and user.password == password:
                self.isLoggedIn = True 
                self.currentUser = user
                print('Bilgi Ekranı'.center(50,'-'))
                print('Login yapıldı.')
                break   # login işlemi yapıldı yani for döngüsünden çıkılsın.
            else:
                
                print('kullanıcı adı veya parola hatalı')


    def logout(self):     
        self.isLoggedIn = False
        self.currentUser = {}
        print('Bilgi Ekranı'.center(50,'-'))
        print('Çıkış yapıldı')

    def identity(self):
        if self.isLoggedIn:
            print('Bilgi Ekranı'.center(50,'-'))
            print(f'username: {self.currentUser.username}')
        else:
            print('Bilgi Ekranı'.center(50,'-'))
            print('giriş yapılmadı.')


    def savetoFile(self):   # bilgileri alıp json bilgisi olarak data base e kayıt edecek.
        list = []  # aşağıda json stringe çevirdiklerimizi buraya atıyoruz
        # bilgileri tek tek jsonstringe çevircez ki atabilelim
        for user in self.users: 
            list.append(json.dumps(user.__dict__))   # dumps jsonstringe çeviriyor
                    # user classını dict den json stringe çevirirken, user bir dict olmadığı bir class olduğu için user classını bir dicte dönüştürmek için user.__dict__ metodunu kullandık öncesinde zaten onu json stringe çevirecek kodu da yazdık
        with open('15 ] İleri Seviye Modüller/users.json','w') as file: # içinde bilgi var ise siler w modu
            json.dump(list, file)   # liste dosyaya kayıt edilecek





repository = UserRepository()   # döngü her döngüğünde sıfırlanmasın diye repositoriyi döngünün dışında tuttuk.










while True:
    print('Menü'.center(50,'-'))    # .center görmüştük daha önce
    secim = input('1- Register\n2- Login\n3- Logout\n4 - Identity\n5 - Exit\n seçiminiz: ')
    if secim == '5':
        break   # while true ile sonsuz döngü yaptık break ile çıkacak
    else:
        if secim == '1':
            username = input('username: ')
            password = input('password: ')
            email = input('mail: ')

            # yukardan gelen bilgilerle bir user oluştursun alltta (user classından user nesnesi)
            user = User(username = username, password = password, email = email) # = koyup birdaha yazma nedeni hata yapma durumuna ...önlem
            repository.register(user)

            print('Bilgi Ekranı'.center(50,'-'))
            print(repository.users)

        elif secim == '2':  # login 
            if repository.isLoggedIn:
                print('Bilgi Ekranı'.center(50,'-'))
                print('zaten giriş yaptınız')
            else:
                username = input('username: ')
                password = input('parola: ')
                repository.login(username, password)

        elif secim == '3':  # logout
            repository.logout()
        
        elif secim == '4': # identity (display username)
            repository.identity()
        else:
            print('Bilgi Ekranı'.center(50,'-'))
            print('yanlış seçim')
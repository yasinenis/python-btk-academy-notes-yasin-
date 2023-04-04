def sayHello():
    print('Hello')

sayHello() # burada fonksiyonu çağırmış oluyoruz...
# ...fonksiyonu çağırmazsak fonksiyon bloğu içindeki kodlar çalışmaz

print('🍚test 1 passed')

# FONKSİYONA PARAMETRE GÖNDERME
# fonksiyona dışarıdan bir parametre de gönderebiliriz

def sayHello(name):   
    print('Hello ' + name)

sayHello('Çınar')    # dışardan çınar parametresi gönderdik


print('🍚test 2 passed')


# sayHello() parantez boş olursa (parametre belirtmezsek) 

def sayHello(name = 'user'):
    print('Hello ' + name)

sayHello('Çınar')
sayHello('Ada')
sayHello()   # boş bırakırsan user der

print('🍚test 3 passed')

# peki ekrana printi yazmak yerine biz fonksiyona dışardan bir bilgi gönderelim ve
# ve bize bir string bir ifade oluştursun ve bunu bize geri göndersin istiyorum

def sayHello(name = 'user'):
    return('Hello ' + name)    # return : parantez içinin fonksiyondan geriye gönderilmesini sağlar

msg = sayHello('Çınar')
print(msg)

print('🍚test 4 passed')

# toplama örneği

def total(num1, num2):
    return num1 + num2

result = total(20, 30)
print(result)


# yaş hesaplama örneği

def yasHesapla(dogumYili):
    return 2023 - dogumYili

ageCinar = yasHesapla(2017)
ageAda = yasHesapla(2010)
ageSena = yasHesapla(1999)

print(ageAda, ageCinar, ageSena)

# emekliliğe kaç yıl kaldı hesapla (yukardaki fonksiyondan yararlandık bir yerde)

def EmekliligeKacYilKaldi(dogumYili, isim):
    '''
    DOCSTRING: Doğum yiliniza gore emekliliğinize kac yil kaldı
    INPUT: Dogum yili
    OUTPUT: Hesaplanan yil bilgisi

    '''
    yas = yasHesapla(dogumYili)
    emeklilik = 65 - yas

    if emeklilik > 0 :
        print(f'emekliliğinize {emeklilik} yıl kaldı    ')
    else:
        print('zaten emekli oldunuz')

EmekliligeKacYilKaldi(2001, 'Yasin') # yaptığımız fonksiyonu çağırdık.

# herhangi bir fonksiyonu kullanmadan önce
print(help(EmekliligeKacYilKaldi))    # help + (fonksiyon ismi)

# fonksiyonun kullanım şekli gibi bilgileri verir.
# NOT: bu kodun vereceği bilgiyi sizin fonksiyonun içine string olarak yazmanız lazım önceden.
# bakınız 66-71 satırları arası.

# help komutu başka bir yerdeki işleyişi

list = [1, 2, 3]

print(help(list.append))   # help komutu burada da append metodunun ne iş yaptığını anlatır terminalde.
'''

ogrenciler = {
    '120' : {
        'ad' : 'Ali',
        'soyad' : 'Yilmaz',
        'telefon' : '538656523'
    },
    '125' : {
        'ad' : 'Can',
        'soyad' : 'Korkmaz',
        'telefon' : '05273627'
    },
    '128' : {
        'ad' : 'Volkan',
        'soyad' : 'Yükselen',
        'telefon' : '538297723'
    },
}

1- Bilgileri verilen öğrencileri kullanicidan aldiğiniz bilgilerle dictionary içinde saklayiniz.

2- Öğrenci numarasini kullanicidan alip ilgili öğrenci bilgisini gösterin


'''


ogrenciler = {}

number = input("öğrenci no: ")

name = input("öğrenci adı: ")

surname = input("öğrenci soyad: ")

phone = input("öğrenci telefon : ")

ogrenciler[number] = {
    'ad' : name,
    'soyad' : surname,
    'telefon' : phone
}

print(ogrenciler)

# yukarıdaki işlemlerin aynısını update metoduyla da yapabiliriz

number = input("öğrenci no: ")

name = input("öğrenci adı: ")

surname = input("öğrenci soyad: ")

phone = input("öğrenci telefon : ")


ogrenciler.update({                    # update ile birden fazla veriyi liste uzerine ekleme şansınız var
    number: {
        'ad' : name,
        'soyad' : surname,
        'telefon' : phone
    }
})

# 3. öğrencinin bilgilerini de isteyelim

number = input("öğrenci no: ")

name = input("öğrenci adı: ")

surname = input("öğrenci soyad: ")

phone = input("öğrenci telefon : ")

ogrenciler.update({                    
    number: {
        'ad' : name,
        'soyad' : surname,
        'telefon' : phone
    }
})

print(ogrenciler)

# 2. soruya geçelim

print('*'*50)

ogrNo = input('öğrenci no: ')
ogrenci = ogrenciler[ogrNo]

print(ogrenci)

print(f"Aradığınız {ogrNo} nolu öğrencinin \nadı: {ogrenci['ad']} \nsoyadı: {ogrenci['soyad']} \ntelefon: {ogrenci['telefon']}")


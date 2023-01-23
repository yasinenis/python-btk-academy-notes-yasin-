# Dictionary liste tipi key - value seklinde çalışır
# +yanibir bilgiye ulaşmak için key bilgisini kullanıyoruz

sehirler = ['kocaeli','istanbul']
plakalar = [41, 34]

print(plakalar[sehirler.index('kocaeli')])    # plakalar[41] yazsak mesela 41 i çekiek ya listeden . onun yerine kocaelinin şehirler listesindeki indeksi kaçsa (indeks sıfır)  aynı indexteki bilgiyi plakalar listesinden seç demek istedik

print(plakalar[sehirler.index('istanbul')])   # aynısını istanbulun indexiyle aynı indexteki bilgiyi plakalarda bulmak için yaptık

# bizim burda yaptığımızı dictionary ile daha kolay yapıcaz
# mesela . 
# print(plakalar['kocaeli']) bizi direk 41 e götürecek
# print(plakalar['istanbul']) bizi direk 34 e götürecek

#--------------------------------------------

# tanimlananBilgi = { 'key'  : 'value', 'key2' : 'value2'}

plakalar = { 'kocaeli' : 41, 'istanbul' : 34 }
print(plakalar['kocaeli'])     # 41 verdi terminal

print(plakalar['istanbul'])    # 34 verdi

# key /value ekleyelim

plakalar['ankara'] = 6    # ankarayı key 6 yı value olarak ekledik
print(plakalar)

plakalar['kocaeli'] = 'new value' # var olan bir keye karşılık geliyosa value eklemiş oluruz
print(plakalar)


#---------------------------------------------

users = {
    'sadikturan' : 36,
    'cinarturan' : 2
}

print(users['cinarturan'])

#---------------------------------------------
# alt bilgiler ekleyebiliriz

users = {
    'sadikturan' : {
        'age' : 36,
        'roles' : ['user'],     # roles sonradan ekledik 
        'email' : 'sadik@gmail.com',
        'adress' : 'kocaeli',
        'phone' : '05235623525'
    },
    'cinarturan' : {
        'age' : 2,
        'roles' : ['admin','user'],     # roles sonradan ekledik
        'email' : 'cinar@gmail.com',
        'adress' : 'kocaeli',
        'phone' : '23231234355'
    }
}

print(users['cinarturan'])    # cinarturan hakkındaki tüm bilgileri verdi

# peki bilgilere nasıl ayrı ayrı ulaşacağız
print(users['cinarturan']['age'])    # yaş bilgisine ulaştık 2
print(users['cinarturan']['email'])
print(users['cinarturan']['adress'])

# sonradan eklediğimiz roles klasorune de ulaşmaya çalışalım

print(users['cinarturan']['roles'][0])    # roles in 0. indeksinde de admin varmış
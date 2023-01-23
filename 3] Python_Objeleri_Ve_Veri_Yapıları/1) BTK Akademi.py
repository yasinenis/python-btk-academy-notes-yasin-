#BTK Akademi Python Kursu
print(94+17+100)
print('30 günde bitmesi için günde?')
print(211/30)
print('60 günde bitmesi için günde?')
print(211/60)
print('ya günde 4 video ya da 8 video')
#SAYI VERİ TİPLERİ INTEGER / FLOAT

#     Integer,örnek 5 , 25 , -23 gibi tam sayılar
#     Float ise örnek 5.2 , 3.2333 , 0.0 gibi virgüllü sayılar 

'type()' #komutunundki parantez içine herhangi bir şey yazarsak bize o verinin tipini söyler 
#örnek
type(2) #terminale yazarsak çıktı -> <class 'int'> der
type(2.0) #     ''      ''     ''  -> <class 'float'> der

#Math Operators
# toplama + Çıkarma - Çarpma * Bölme / Üs ** Mod % Tam bölme //
print(2**3) #üç üssü iki demektir yani 8 yapar
print(14/3) #terminalde 4.6 gibi bi cevap verir
print(14//3)#terminalde 4 değerini verir virgülsüz hali .

#DEĞİŞKEN TANIMLAMA VE KURALLARI

#rakam ile baslayamaz 

number1 = 20
print(number1) #ne yazacağını biliyosun

number1 += 30 #NOT (!) += isareti önceden 20 tanımlamıştı yeniden tanımlıyorum ve onun da uzerine 30 ekliyorum demek istedik (+= isaretiyle kast edilen anlam bu)
print(number1)

#değişken tanımlarken büyük küçük harf duyarlılığı vardır . ( print(kitap)ile print(KİTAP) Aynı sey değildir )

#   ''        ''     türkçe karakter kullanma (mesela ş,)

x = 1                   #Integer 
y= 2.6                  #Float
name = ('mehmet')    #String
isStudent = False       #bool

#Yukarıdaki tanımlamayı tek satırda da yapabiliriz:
x, y, name, isStudent = (1, 2.6, 'mehmet', False) 

a = 10
b = 20
print(a+b)   #terminal 30 der 

a = '10'
b = '20'
print(a+b)   #terminal 1020 der 

#VERİ TİPİ DÖNÜŞÜMLERİ

#örnekteki problemi çöz
x = input('1.Sayi')
y = input('2.Sayi')

toplam = x + y

print(toplam)

#yukarıda kullanıcı terminalde sorulan x'e hangi değeri gireceksiniz sorularında x'e 10 y'ye 20 girerse
#sonucu 1020 yazıyor halbuki biz 10 + 20 den 30 olmasını istiyoruz

#çözüm
x = input('1.Sayi')
y = input('2.Sayi')

print(type(x))
print(type(y))

toplam = int(x) + int(y)

print(toplam)

#not : print(type(a)) dersen a nın tipini yaz demek istersin . 
''' a bir string integer float bool olabilir '''





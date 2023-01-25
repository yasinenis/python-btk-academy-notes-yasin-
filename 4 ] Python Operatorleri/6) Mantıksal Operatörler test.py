'''# 1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.

sayi = int(input('Bir sayi Giriniz : '))
result = ( 0 < sayi < 100 )
print(result)

# 2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.

sayi = int(input('Tekrar bir sayı giriniz : '))
result = ( sayi %2 == 0 ) and (sayi > 0)
print(f'Girilen sayının çift olma durumu : {result} ')

# 3- Email ve parola bilgileri ile giriş kontrolü yapınız.
email = 'yasin.artvin@gmail.com'
password = '0088089'

girilenEmail = input('Lütfen email giriniz.. : ')
girilenSifre = input('Lütfen Şifre Giriniz.. : ')

result = (email == girilenEmail) and (password == girilenSifre)
print(f'Girilen Giriş blgilerinin doğruluğu {result} ')  

# 4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.

a = input('a: ')
b = input('b: ')
c = input('c: ')

result = (a > b) and (a > c)
print(f'a en büyük : {result} ')

result = (b > a) and (b > c)
print(f'b en büyük : {result} ')

result = (c > a) and (c > b)
print(f'c en büyük : {result} ')

# 5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
#    Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın .
#    a-) Ortalama 50 olsa bile final notu en az 50 olmalıdır.
#    b-) Finalden 70 alındığında ortalamanın önemi olmasın.

vize1 = float(input('Vize1 : '))
vize2 = float(input('Vize2 : '))
final = float(input('Final : '))

ortalama = ((vize1 + vize2)/2 * 0.60) + (final * 0.4)

result = (ortalama >= 50)
print(f'ortalamanız : {ortalama} ')
print(f'ilk durumda geçme durumunuz : {result} ')

resulta = (ortalama == 50) and (final >= 50)
print(f'a sorusuna göre geçme durumu : {resulta} ')

resultb = (ortalama >= 50) or (final >= 70)
print(f'b seçeneğine göre geçme durumu : {resultb}')
'''
# 6- Kişinin ad, kilo ve boy bilgilerini alıp kilo endekslerini hesaplayınız.
#    Formül: (Kilo / boy uzunluğunun karesi)
#    Aşağıdaki tabloya göre kişi hangi gruba girmektedir.
#    0 - 18.4        => zayıf
#    18.5 - 24.9     => Normal
#    25.0 - 29.9     => Fazla Kilolu
#    30.0 - 34.9     => Şişman (Obez)

name = input('İsminiz : ')
weight = float(input('Lütfen Kilonuzu Girin : '))
hight = float(input('Boyunuzu Girin : '))

index = ( weight / (hight **2) )  

zayif = (index >= 0) and (index <= 18.4)
normal = (index > 18.4) and (index <= 24.9)
kilolu = (index > 24.9) and (index <= 29.9)
obez = (index >= 29.9) and (index <= 34.9)


print(f' {name} kilo indeksin: {index} ve kilo değerlendirmen zayıf: {zayif} ')
print(f' {name} kilo indeksin: {index} ve kilo değerlendirmen normal: {normal} ')
print(f' {name} kilo indeksin: {index} ve kilo değerlendirmen kilolu: {kilolu} ')
print(f' {name} kilo indeksin: {index} ve kilo değerlendirmen obez: {obez} ')

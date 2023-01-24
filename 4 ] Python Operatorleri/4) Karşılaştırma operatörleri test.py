# 1- Girilen 2 sayıdan hangisi büyüktür ?

a = int(input('Bir sayi giriniz : '))
b = int(input('Yeni bir sayi giriniz : '))

result = (a > b)
print(f'a: {a}, b: {b} den büyüktür: {result}')

# 2- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız
#     eğer ortalama 50 ve üstündese geçti dğilse kaldı yazdırın

v1 = float(input('İlk Vize notunuzu girin : '))
v2 = float(input('İkinci Vize notunuzu girin : '))
final = float(input('Final notunuzu girin : '))

ortalama = (((v1 + v2)/2) * 0.6) + (final * 0.4)

print(f'not ortalamanız : {ortalama} ve dersten geçme durumunuz: {ortalama>=50} ')

# 3- Girilen bir sayının tek mi çift mi olduğunu yazdırın .

sayi = int(input('Sayı Giriniz : '))

tekcift = (sayi % 2 == 0)    # herhangi bir sayının mod 2 'si kalan 0 oluyorsa çift sayıdır
#                                                   mod : bölme işlemi yapıp kalanı aldığınız demek

print(f'girilen sayı çift olma durumu : {tekcift} ')

# 4- Girilen bir sayının negatif pozitif durumunu yazdırın.

sayi = int(input('Bir sayi giriniz : '))

result = ( sayi > 0 )

print(f'{sayi} sayısının pozitif olma durumu : {result} ')

# 5- Parola ve email bilgisini isteyip doğruluğunu kontrol ediniz.
#     (email: email@sadikturan.com parola:abc123)

email = 'email@sadikturan.com'
password = 'abc123'

girilenEmail = input('Lütfen emailinizi yazın : ')
girilenSifre = input('Lütfen şifrenizi yazın : ')

kontrolEmail = girilenEmail == email
kontrolSifre = girilenSifre == password

print(f'email durumu : {kontrolEmail}, şifre durumu : {kontrolSifre} ')

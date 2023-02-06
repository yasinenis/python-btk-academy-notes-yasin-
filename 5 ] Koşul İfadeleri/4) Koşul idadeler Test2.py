# 1- Girilen sayının 0-100 arasında olup olmadığını kontrol edin
sayi = (input('Bir sayı gir : '))

if (0 < int(sayi) < 100) :
    print("Sayı 0-100 Arasındadır :) ")
elif (int(sayi) == 0) :
    print('Sayı 0 dır')
elif (int(sayi) == 100):
    print('Sayı 100 dür')
elif (int(sayi) < 0) or (sayi > 100):
    print('sayı 0-100 arasında veya eşit değil')
else:
    print(f"Girdiğin {sayi} adam gibi bir sayı değil  :(")

# 2- Girilen bir sayının pzitif çift sayı olup olmadığını kontrol edin

sayi = int(input('Bir sayı girin : '))

if (sayi % 2 == 0 ):
    print('Çift sayıdır')
else:
    print('Tek sayıdır')

# 3- Email ve parola bilgileri ile giriş kontrolü yapınız
#         email : email@sadikturan.com
#         password : abc123
email = "email@sadikturan.com"
password = "abc123"

girilenEmail = input('Email : ')
girilenSifre = input('Sifre : ')
if (girilenSifre == email) and (girilenEmail == password):
    if (girilenEmail == email):
        if (girilenSifre == password):
            print('Başarıyla Giriş Yaptınız')
        else:
            print('Şifre Yanlış')
    else:
        print('Email Yanlış')
else:
    print('Email Ve Şifre HATALI')


# 4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız

sayi1 = int(input('İlk Sayı : '))
sayi2 = int(input('İkinci Sayı : '))
sayi3 = int(input('Son Sayı : '))

if (sayi1 > sayi2 > sayi3) :
    print(f'{sayi1} > {sayi2} > {sayi3}')
elif (sayi1 > sayi3 > sayi2) :
    print(f'{sayi1} > {sayi3} > {sayi2}')
elif (sayi2 > sayi1 > sayi3) :
    print(f'{sayi2} > {sayi1} > {sayi3}')
elif (sayi2 > sayi3 > sayi1) :
    print(f'{sayi2} > {sayi3} > {sayi1}')
elif (sayi3 > sayi1 > sayi2) :
    print(f'{sayi3} > {sayi1} > {sayi2}')
elif (sayi3 > sayi2 > sayi1) :
    print(f'{sayi3} > {sayi2} > {sayi1}')
else:
    print('Ne oldu anlamadım ama garip şeyler yapıyorsun')

# 5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
#         Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın
#          a-) Ortalama 50 olsa bile final notu en az 50 olmalıdır
#          b-) Finalden 70 alındığında ortalamanın önemi olmasın

vize1 = int(input('Vize1 : '))
vize2 = int(input('Vize2 : '))
final = int(input('Final : '))

ort = ((vize1 + vize2) /2 * 0.60 ) + (final * 0.40)

if (ort >= 50):
    print('Geçtiniz')
else:
    print('kaldınız')
# b) şıkkı nın cevabı

if (ort >= 50) and (final >= 50):
    print('B KOŞULUNU DA -- Geçtiniz')
else:
    print('B KOŞULUNU -- Geçemediniz ')
# c) şıkı nın cevabı

if (ort >= 50) or (final >= 70):
    print('C KOŞULUNA GÖRE -- Geçtiniz')
else:
    print('C KOŞULUNA GÖRE -- Geçemediniz')


# 6- Kişinin ad , kilo ve boy bilgilerini alıp kilo endekslerini hesaplayınız.
#         Formül: (kilo / boy uzunluğunun karesi)
#         0-18.4  =>   Zayıf 
#         18.5-24.9  =>   Normal 
#         25.0-29.9  =>   Fazla Kilolu 
#         30.0-34.9  =>   Şişman(Obez)

name = input('İsminiz : ')

kilo = float(input('Kilonuz : '))
boy = float(input('Boyunuz : '))

index = kilo / boy * 2

if (0 <= index <= 18.4):
    print('Kilo indexsiniz Zayıf')
elif (18.5 <= index <= 24.9):
    print('Kilo indexsiniz Normal')
elif (25.0 <= index <= 29.9):
    print('Kilo indexsiniz Fazla Kilolu')
elif (30.0 <= index <= 34.9):
    print('Kilo indexsiniz Şişman Obez')
else:
    print('sanırım garip bir şey tuşladınız')




# elimizde bir liste yoksa ve 1 'den 100 'e kadar sayıları ekranda yazdırmak istersem:
#cevap : birden 100 e kadar sayıları bir listeye atıp for döngüsüyle yazdırmak amele işi
# bunun yerine : 

x = 0     # ile baslayıp bir ekleyerek devam etsin koşul tamamlanınca false değeri gelsin işlem dursun (while döngüsü)

'''

while True:       # true olunca durmadan 0 yazar.
    print(x) 

'''

# bu islemi bi yerde kesmemiz lazım . sonsuza kadar devam etmesin

'''

while x <= 100:       # x 100 den küçük eşit olana kadar true değerini verir 101 de false olur durur döngü
    print(x)          # 100 olana kadar (false olana kadar) x yazar sonra x 'e bir ekler döngü devam eder
    x = x + 1


print('bitti...')


'''
'''


x = 1
while x <= 100:
    if x % 2==0:    # eğer çit ise x 'i yazdır demek istiyor . 
        print(x)    # döngü 1 artarak devam ediyor fakat fark şurda çift ise yaz anlamında .
    x += 1

print('bitti...')


'''


while x <= 100:
    if x % 2 == 0:
        print(f'{x} : çift ')
    else:
        print(f'{x} : tek')
    x = x + 1


name = ''     # false 'ye karşılık gelir.
while not name.strip():        # isim girmek yerine mesela 5 kez bosluk tusuna basarsak kabul etmesin diye strip() komutunu kulllandık
    name = input('isminizi giriniz : ')


print(f'Merhaba, {name}')









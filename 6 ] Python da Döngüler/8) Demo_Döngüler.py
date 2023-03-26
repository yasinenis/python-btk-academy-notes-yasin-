'''
1-100 arasinda rastgele üretilecek bir sayiyi aşaği yukari ifadeleri ile
buldurmaya çalişin.(hak=5)
    ** "random modülü" için "python random" şeklinde arama yapin.
    ** 100 üzerinden puanlama yapin. Her soru 20 puan.
    ** Hak bilgisini kullanicidan alin ve her soru belirtilen can sayisi
    üzerinden hesaplansin.
'''

import random


""" 

sayi = random.randint(1,10)        # random modülünden bir komut: 1 ile 100 arası rastgele integer bir sayı seçtirdik
hak = 5

while hak > 0:
    hak -= 1
    tahmin = int(input("tahmininiz : "))

    if sayi == tahmin:
        print("Tebrikler sayıyı bildiniz")
        break                                    # break komutu döngüden çıkartır
    elif sayi > tahmin:
        print("Yukarı")
    else:
        print("Aşağı")

    if hak == 0:
        print(f"hakkınız bitti tutulan sayı şuydu : {sayi} ") 

"""


# kaçıncı defada bildiğimizi göstermek için değişiklik yapalım
# (değiştirdiğimiz satırlara #d ekledim)


""" 

sayi = random.randint(1,10)        
hak = 5
sayac = 0           #d

while hak > 0:
    hak -= 1
    sayac += 1          #d
    tahmin = int(input("tahmininiz : "))

    if sayi == tahmin:
        print(f'Tebrikler {sayac}. defada sayıyı bildiniz')         #d
        break                                    
    elif sayi > tahmin:
        print("Yukarı")
    else:
        print("Aşağı")

    if hak == 0:
        print(f"hakkınız bitti tutulan sayı şuydu : {sayi} ") 

"""

# şimdi 100 üzerinden puanlama yapalım her soru 20 puan olsun

""" 

sayi = random.randint(1,10)        
hak = 5
sayac = 0           

while hak > 0:
    hak -= 1
    sayac += 1          
    tahmin = int(input("tahmininiz : "))

    if sayi == tahmin:
        print(f'Tebrikler {sayac}. defada sayıyı bildiniz. Toplam puanınız: {100 - (20)* (sayac-1)}')  # soruyu bildiği turun puanını kaybetmesin diye -1 dedik       
        break                                    
    elif sayi > tahmin:
        print("Yukarı")
    else:
        print("Aşağı")

    if hak == 0:
        print(f"hakkınız bitti tutulan sayı şuydu : {sayi} ") 
        
"""

# şimdi hak bilgisini kulanıcıdan alalım. her soru belirtilen can sayısı üzerinden hesaplansın

sayi = random.randint(1,10)     
can = int(input("kaç hak kullanmak istersiniz? : "))        #d
hak = can                                                  #d
sayac = 0           

while hak > 0:
    hak -= 1
    sayac += 1          
    tahmin = int(input("tahmininiz : "))

    if sayi == tahmin:
        print(f'Tebrikler {sayac}. defada sayıyı bildiniz. Toplam puanınız: {100 - (100/can)* (sayac-1)}')      #d    
        break                                    
    elif sayi > tahmin:
        print("Yukarı")
    else:
        print("Aşağı")

    if hak == 0:
        print(f"hakkınız bitti tutulan sayı şuydu : {sayi} ")
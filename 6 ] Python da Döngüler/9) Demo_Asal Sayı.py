'''
Soru: Girilen bir sayinin asal olup olmadiğini bulun.
** Asal sayi 1 ve kendisi hariç tam böleni olmayan 
   sayilara deniz
'''
sayi = int(input("Lütfen bir sayi giriniz : "))

asalmi = True

if sayi == 1:
    asalmi = False

for i in range(2, sayi):  # 2 'den seçtiğimiz sayıya kadar sayi nin tam sayı böleni var mı onu kontrol edicez
    if sayi % i == 0:    # sayı nın mod i'si sıfırsa kalansız bölünüyo deriz. asal olmaz ozaman
        asalmi = False
        break
    
    
if asalmi == True:
    print(f"{sayi} asaldır")    
else:
    print(f"Sayı {sayi} asal değildir")  
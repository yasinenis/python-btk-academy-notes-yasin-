sayilar = [1,3,5,7,9,12,19,21]

# 1: sayilar listesini while ile ekrana yazdırın.

i = 0
while (i < len(sayilar)):      
    print(sayilar[i])           # liste içinden eleman yazdırdığımız için indexe göre while kuruyoruz
    i += 1 

# 2: Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki rüm
#    tek sayıları ekrana yazdırın.

baslangic = int(input('ilk değeri : '))
bitis = int(input('bitis değeri : '))

a = baslangic
while (a <= bitis):
    if (a % 2 == 1):
        print(a)
    a += 1

# 3: 1-100 arasındaki sayıları azalan şekilde yazdırın .

a = 100 
while (a > 0):
    print(a)
    a -= 1 

# 4: kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde yazdırın .

numbers = []

i = 0

while (i < 5):
    sayi = int(input('Sayı Gir Uşak'))
    numbers.append(sayi) 
    i += 1

numbers.sort()

print(numbers)

# 5: Kullanıcıdan alacağınız sınırsız ürün bilgisini urunler listeri içinde saklayınız.
#    ** ürün sayısını kullanıcıya sorun .
#    ** dictionary listesi yapısı  (name, price) şeklinde olsun.
#    ** ürüm ekleme işlemi bittiğinde ürünleri ekranda while ile listeleyin.

urunler = []

adet = int(input('Kaç adet ürün eklemek istiyorsunuz ? : '))

i = 0
while (i < adet):
    name = input('ürün ismi : ')
    price = input('fiyatı : ')
    urunler.append({
        'name': name,
        'price': price 
    })
    i += 1

for urun in urunler:
    print(f"ürün : {urun['name']}  fiyatı : {urun['price']} ")



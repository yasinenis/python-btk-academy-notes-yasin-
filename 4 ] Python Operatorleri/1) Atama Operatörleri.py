x = 5
y = 10
z = 20

# ya da tek satırda yapalım
x,y,z = 5, 10, 20

print(x, y, z)

# x içersine 10 veya y içersine 5 değerini atmak istiyorum
x, y = y, x 
print(x, y, z)

x,y,z = 5, 16, 20 # tekrar tanımlayalım

x = x + 5
#bunu yerine şunu yapailiriz
x += 5   # x 'in mevcut değerini toplar 5 'le
x -= 5   # bu da çıkardı
x *= 5   # çarpar
x /= 5   # böler
x %= 5   # x 'in mod unu alır
y //= 5  # tam bölme islemi
y **= 5  # üs alma operatörü

print(x, y, z)

###

# atama operatörlerini liste üzerinde nasıl kullanacağız ona bakıcaz

values = 1, 2, 3        # values isimli bir tuple nesne oluşturduk

print(values)
print(type(values))      # values tuple'mı görelim

# values 'daki 1 2 3 değerlerini x y z değerleri içine direk aktarmak istiyoruz
x, y, z = values

print(x, y, z)

# x,y,z ye tanımlarken valuesdeki elemanları;
# valuesde 3 elemandan az eleman sayısı olsa ( hata verir)
# values de 3 elemandan fazla  ''  ''  ''     (hata verir)

values = 1, 2, 3, 4, 5
x, y, *z = values     # z 'deki * işareti kalan sayıları hepsini z ye tanımla demek liste içinde

print(x, y, z)

# bu durumda z deki istediğimiz elmana ulaşmak için:
print(x, y, z[0])    # x y ve z nin 0. indeksindekine ulaşırız
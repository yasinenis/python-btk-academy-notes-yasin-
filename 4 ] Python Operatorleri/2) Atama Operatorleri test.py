x, y, z = 2, 5, 10

numbers = 1, 5, 7, 10, 6

# 1) Kullanıcıdan aldığınız 2 sayının çarpımı ile x,y,z toplamının farkı nedir?

a = input('Bir sayı girin : ')
b = input('Tekrar bir sayı girin : ')
print(int(a) * int(b) - (x + y + z))

# 2) y' nin x' e kalansız bölümünü hesaplayınız

print(y // x)

# 3) (x,y,z) toplamının mod 3' ü nedir?

toplam = x+y+z
print(toplam % 3)

# 4) y' nin x. kuvvetini hesaplayınız.

result = y ** x     # y 'nin ikinci kuvveti demek

# 5) x, *y, z = numbers işlemine göre z' nin küpü kaçtır?

x, *y, z = numbers # böyle yaparsak x 'e 1 verir z 'ye 6 verir . geri kalan y 'nin olur.

print(z**3)

# 6) x, *y, z = numbers işlemine göre y nin değerleri toplamı kaçtır?

x, *y, z = numbers 

result = y[0] + y[1] + y[2]
print(result)


'''SORU

Daire Alani    : πr²
Daire Çevresi  : 2πr

*Yri çapi verilen bir dairenin alan ve çevresini hesaplayınız . (r = 3.14) '''

r = input('yarı çap giriniz')

r = int(r)
pi = 3.14

alan = pi * (r ** 2)
Cevre = 2 * pi * r

print('hesaplama tamamlandı...')
print('D.Alanı :', alan)
print('D.Cevresi :', Cevre)

print('Tek satırda yazılmak üzere tekrar hesaplanıyor')

alan = str(alan)
Cevre = str(Cevre)
print('D.Alanı :'+ alan + ' ' + 'D.Cevresi :' + Cevre)

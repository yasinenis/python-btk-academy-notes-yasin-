x = int(input('x: '))
y = int(input('y: '))

if x > y:     # if in sağ tarafı belirliyor True ise if in altı False ise elsenin altı çalışıyor
    print('x, y den büyük')
elif x == y:     # elif komutu da farklı bir senaryo için kendince ayrı bir cevap verilmesini sağladı
    print('x y eşit')
else:         # false ise else nin altını çalıştırıyor
    print('y, x den büyük')

# istediğimiz kadar elif komutu yaparak her türlü durumu kontrol edebiliriz

##----------------------

num = int(input('sayı: '))

if num > 0:
    print('sayı pozitif')
elif num < 0:
    print('sayı negatif')
else:                         # diğer kalan tüm durumlar anlamına geliyor burda suan else
    print('sayı sıfır')
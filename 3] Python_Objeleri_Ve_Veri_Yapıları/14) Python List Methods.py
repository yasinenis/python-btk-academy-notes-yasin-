numbers = [1, 10, 5, 16, 4, 9, 10]
letters = ['a', 'g', 's', 'b', 'y', 'a', 's']

val = min(numbers)    # val diye bisey salladık bu numbersin içinden en küçük sayı olarak tanımladık.
val = max(numbers)    # buda max hali
print(val)
 
val = min(letters)    # bu sefer letters için uygularsak alfabedik olarak minimum değeri bulup tanımlar kendini onunla
val = max(letters)    # bu da max hali
print(val)

# liste elemanlarını parçalamak istersek nasıl yapabiliriz

val = numbers[3:6]      # 3 den 6 ya kadar olanı tanımladık
val = numbers[:3]       # bastan basla 3 e kadar git demek
val = numbers[4:]       # 4 den basla sona kadar git 

print(val)

numbers[4] = 40        # 4 indeksteki bilgiyi 40 ile değiştik
print(numbers)

numbers.append('49')   # listeye eleman ekliyor . en sağa ekler
print(numbers)

numbers.insert(3, 78) # istediğin yere ekler . 3. indeksin önüne 78 rakamı eklemis olduk (yani 3. indekse ekliyoda önceden 3. indekste olanı ir sağa kaydırıyor onu 4. indeks e atıyor)
numbers.insert(-1,52) # -1 dediğimiz için en sona ekledi 52'yi

print(numbers)

# peki elemanları nasıl silicez

numbers.pop()     # en sondaki elemanı siler
numbers.pop(0)    # hangi numarayı yazarsan o indeksi siler . ( bu 0. indeksi sildi)
numbers.remove(16) # 16 rakamını siler
print(numbers)

# sıralama işlemleri

numbers.sort()      # bu listeyi sayısal büyüklük olarak sıralar (sayısal veriler olan liste olduğu için)
letters.sort()      # alfabetik olarak sıralar (alfabetik liste olduğu için)

print(numbers)
print(letters)

numbers.reverse()   # sayısal olarak küçükten büyüğe ise ters çevirir ve büyükden küçüğe yapar(numbers sayılardan olusan bir liste old. için)
letters.reverse()   # harflerden oluşan bir liste old. için a dan z ye ise z den a ya doğru sıralar

print(numbers)
print(letters)

print(len(numbers))    # numbers listesinin kkarakter uzunluğu (bildiğin kod)
print(len(letters))    # letters listesinin uzunluğu

print(numbers.count(10))     # count metodunu kullanıp kaç tane 10 sayısı olduğunu bulduk (bildiğin kod burda da kullanılabilir)
print(letters.count('a'))    # aynısının letter listesi için... a dan kaç tane var onu sorduk

numbers.clear()      # tüm elemanları sildi şerefsiz kod
print(numbers)
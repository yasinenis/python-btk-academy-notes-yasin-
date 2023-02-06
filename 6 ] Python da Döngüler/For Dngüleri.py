numbers = [1,2,3,4,5]

print(numbers[0])
print(numbers[1])
print(numbers[2])
print(numbers[3])
print(numbers[4])   # for bilmesek , numberstaki tüm sayıları sırayla bu sekil yazdırabiliriz
# fakat for döngüsü ile daha kolay bi sekilde yazabiliriz

for num in numbers: # numbers içindeki elemanları num isimli bir değişkene at .
    print(num)      # num yazdır: for döngüsü her döndüğünde num içeriğini sırayl yazdır

for num in numbers:
    print('Hello')   # böyle yaparsan liste elemanları kadar Hello yazar

#--------------------------------------

names = ['çınar','sadık','sena']

for name in names:
    print(f'my name is {name} ')   # my name kısmı sabit name kısmı sırayla yazar

#--------------------------------------

name = 'Sadık Turan'

for n in name:
    print(n)    # str ifadenin her bir karakterini yazar

#--------------------------------------

tuple = (1,2,3,4,5)

for t in tuple:
    print(t)

# eğer liste içine alırsak...

tuple = [(1,2),(1,3),(3,5),(5,7)]

for t in tuple:
    print(t)        # her bir liste elemanı bir tuple listesine karşılık gelir


# eğer onların da içinden tek tek almak istersek ...

tuple = [(1,2),(1,3),(3,5),(5,7)]

for a,b in tuple:     # a ve b yi x,y imiş gibi düşünürsen neden 1 1 3 5 yazdırdığını anlarsın
    print(a)

#--------------------------------------

d = {'K1':1, 'k2':2, 'k3':3}      # eski derslerden dictionary ( key value) seklinde yazdık

for item in d: 
    print(item)       # listedeki sadece key bilgilerini aldı

# eğer eleman gruplarına ulaşmak istersek...

for rastgele in d.items():   # items komutunu kullandık   bknz: önceden işledik benzer omutları
    print(rastgele)          # eleman gruplarına tek tek ulaştık

# eleman gruplarına ulaştıktan sonra
# key ve value bilgilerine ayrı ayrı ulaşmak istersek...

for key,value in d.items():   # yukardaki a,b deki gibi x.y li sisteme ayırmıs gibi olduk
    print(key, value)            # bu satırda sadece key yazsaydın sadece key bilgisine ulaşırdın

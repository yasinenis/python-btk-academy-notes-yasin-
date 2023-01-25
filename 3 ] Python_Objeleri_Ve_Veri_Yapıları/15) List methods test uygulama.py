####        TEST UYGULAMA        ####     



names = ['Ali','Yağmur','Hakan','Deniz']
years = [1998, 2000 , 1998, 1987]

# 1- "Cenk" ismini listenin sonuna ekleyiniz.

names.append('Cenk')
print(names)

# 2- "Sena" değerini listenin başına ekleyiniz.

names.insert(0, 'Sena')   # bu metotla 0 yerine len(names) yazarsan en sona ekler
print(names)

# 3- "Deniz" ismini listeden siliniz.

names.remove('Deniz')
print(names)

''' alternatif hocanin çözümleri'''
names.pop(1)    # mesela b yağmur metodunu siler . içindeki index yağmuru isaret ediyor çünkü
print(names)


''' yeniden tanimlayalim asağidaki sorular için   '''
names = ['Ali','Yağmur','Hakan','Deniz']                


# 4- "Deniz" isminin indeksi nedir?

saçmaKelime = names.index('Deniz')       # bunu hatırladık mı yeni mi öğrendim emin değilim . bir seyin indexini bulmak.
print(saçmaKelime)
    
# 5- "Ali" listenin bir elemanı mıdır?

result = 'Ali' in names           # in komutu listede olup olmadığına bakıyor
print(result)

# 6- Liste elemanlarını ters çevirin.
print(names[::-1])   # hoca bunu kullanmadı . bu da çalışıyor ama.

''' hocanin cevabi'''
names.reverse()
print(names)

# 7- Liste elemanlarını alfabetik olarak sıralayınız.
names = ['Ali','Yağmur','Hakan','Deniz']
cevap = names.sort()
print(cevap)

# 8- years listesini rakamsal büyüklüğe göre sıralayınız.

years.sort()
print(years)

# 9- str = "Chevrolet,Dacia" karakter dizisini listeye çeviriniz.

str = ['Chevrolet','Dacia']
print(str)

''' hocanin demek istediği şu : aşağidaki gibi bilgisayar yapsin bu işi sen eline ver malzemeyi'''

str = "Chevrolet,Dacia"  # bu bilgiyi ver makinanın eline
result = str.split(',')
print(result)

# 10- years dizisinin en büyük v en küçük elemanı nedir?

min = min(years)
max = max(years)
print(min, max)

# 11- years dizisinde kaç tane 1998 değeri vrdır?

result = years.count(1998)
print(result)

# 12- years dizisinin tüm elemanlarını siliniz.

years.clear()
print(years)

# 13- kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız.

markalar = []         # içi boş bir obje tanımladık

marka = input("marka: ")    # kullanıcı markayı atsın diye input kullandık
markalar.append(marka)     # kullanıcının girdiği veriyi listeye atsın diye append metodunu kullandık (listenin sonuna atıyor append)

marka = input("marka: ")     # 3 marka istediği ve döngüyü öğrenmediim için 3 kere yazıcaz
markalar.append(marka)

marka = input("marka: ")
markalar.append(marka)

print(markalar)
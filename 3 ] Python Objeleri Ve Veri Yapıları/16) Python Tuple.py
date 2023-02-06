####   normal liste ve tuple listenin aynı/farklı yönlerini inceliyoruz    ###

list = [1, 2, 3]
tuple = (1, 'iki', 3)

print(type(list))        # <class 'list> dedi tipine
print(type(tuple))       # <class 'tuple> dedi tipine

print(list[2])
print(tuple[2])          # ikisi içinde aynı seçili indexteki veriye bakma yontemi

print(len(tuple))
print(len(list))         # ikisi de aynı

list = ['ali','veli']      #ikisi de aynı
tuple = ('damlar','ayşe')  # dikkat(!) burda bunları eklemedis olmadık kople listeyi bu olarak değiştik

print(list)
print(tuple)

list[0] = 'ali'
'''tuple[0] = 'deniz'    ''' # atama işlemi yapmıyor bu da tuple nin farkı

# sonuç olarak ne öğrendik
# tuple da line 16 daki gibi tüm listeyi yeniden tanımlamış olmak gibi toptan bir atama işlemi yapabiliyosun fakat line 22 deki gibi teker teker bir atama yapamıyosun.

#------------------------------------------
tuple = ('damla','ayşe','ayşe')  #yeniden tanımladık

print(tuple.count('ayşe'))
print(tuple.index('ayşe'))    # 2 tane aşye var ilk nerde varsa onun indexini verdi
print(list)
print(tuple)

#------------------------------------------

tuple = ['damla','ayşe','ayşe']
names = ['demet','emel','ayşe'] + tuple  #tuple ' ı ekledik names listesine

print(names)



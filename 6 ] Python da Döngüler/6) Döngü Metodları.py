# range() 

'''

list = [1,2,3]

for item in list:
    print(item)       #elimizdeki listeyi tek tek ekrana yazdı

'''

# ya eğer elimizde bir liste yoksa?..range kullanabiliriz .

for item in range(10):   # sıfır dan 10 a (on dahil değil) liste oluşturdu
    print(item)

for item in range(2,10): # 2 den basla 10 a kadar git demek
    print(item)          # itemleri tek tek alıp ekrana yazdırabilirim

for item in range(50,100,10): # 10 ar 10 ar artır demek.
    print(item) 

print(list(range(5,100,10)))    # range listeyi olusturuyor zaten bize print etmek kalıyor

#----------------------------------------
#                             enumerate metodu

# eğer biz her ulaştığımız elemanın index bilgisine ulaşmak istersek...
greeting = 'Hello There'

index = 0
for letter in greeting:        # bildiğin gibi kelimeleri sırayla ekrana yazar
    print(f'index : {index}, letter : {letter} ')
    index += 1
# yukarıdaini enumerate metodu ile yapabiliriz
# index isimli bir değişken tanımlamadan indexi bulucaz 

greeting = 'Hello'

for index,letter in enumerate(greeting):           # x,y gibi olmus oldu index,letter kısmı . x,y kısmını daha önce gördük/işledik
    print(f'index: {index} letter: {letter} ')

# yukarıdaki kısmı anlamak için enumerate ' nin sade kullanımı aşağıda

greeting = 'Hello There'

for item in enumerate(greeting):       # index numaraları ve karaktere karşılık gelen elemanları bizim için bir liste halinde tek tek oluşturuyor
    print(item)                       # tek tek ulaimak için 38. satırdaki işlemi yapabiliriz

#----------------------------------------
#                            zip metodu

list1 = [1,2,3,4,5]
list2 = ['a','b','c','d','e']
list3 = [100,200,300,400,500]

zip(list1,list2) # zip metodu burada bir eşleştirme yapar
# sonucu da list medoduyla listeye çevirelim ve yazdıralım
print(list(zip(list1,list2,list3)))

# peki bunları for döngüsünde nasıl kullanırız

for item in zip(list1,list2,list3):
    print(item)      # her bir eleman bir önceki liste elemanlarına karsılık gelerek yazdırılıyor

# her bir elemana ulaşmak istersek...

for a,b,c in zip(list1,list2,list3):
    print(a,b,c)          # liste içersinden çıkıp yan yana yazabildik
    

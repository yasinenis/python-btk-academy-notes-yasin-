# sets listelerinin olayı : index bilgisiyle ulaşamıyosun . 

fruits = { 'orange', 'apple', 'banana' }

# print(fruits[0]) yapamıyosun indexlenemez liste çünkü


# elemanlarına ulaşmk için döngü kullanıcaz henuz dögüleri henüz öğrenmedik
#+ ama elemanlara ulaşmak için ön bilgi olsun

for x in fruits:        # galiba sırayla elemanları x e tanımlıyor
    print(x)            # liste elemanlarını sırayla yazdı

# sets listelerini sıralayamayız

# peki nasıl eleman ekliycez
fruits.add('cherry')
print(fruits)

# veya update ile fruits'in içine liste gönderebiliriz

fruits.update(['mango','grape'])
print(fruits)

# zaten var olan bir şeyi eklemeye çalışalım
fruits.update(['apple'])
print(fruits)      # eklenmez miş zaten var olan bir şey

myList = [1,2,5,4,4,2,1]
print(myList)
print(set(myList))    #tekrarlayan elemanları set komutu listeden sildi

fruits.remove('mango')   # mangoyu sildik (remove) ile
fruits.discard('apple')  # apple'ı sildik (discard) ile

print(fruits)

fruits.pop()     # bu kmut içi boşsa son satırı silerdi fruits indexli bir liste değil yani hangi elemanı silecek Allah bilir 
print(fruits)    # 'banana' yı sildi

fruits.clear()   # Tüm elemanları siler...


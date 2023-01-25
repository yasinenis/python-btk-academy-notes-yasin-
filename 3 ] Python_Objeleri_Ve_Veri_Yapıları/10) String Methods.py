message = 'Hello There. My name is Mehmet Selim'

message = message.upper()    # mesajın tamamını büyük harf yapar

print(message)

message = message.lower()    # mesajın tamamı küçük harf yapar

print(message)

message = message.title()    #   ''    baş harflerini büyük harfe çevirir

print(message)

message = message.capitalize() # Cümlenin sadece baş harfi büyük

print(message)

message = message.strip()    # Cümlenin baş ve sonundaki boşluğu siler

'''message = message.split()''' # Her bir kelime boşluklardan ayrılır ve ayrı ayrı yazılır
                             
 
message = message.split()    # İçine nokta koyarsan noktalardan ayırır . 
# UYARI bunu test etmeden önce etkilenecek diğer satırları yorum satıırına çevir (31 ve 32 etkileniyor)

print(message)

# son kod böldü cümleyi ve biz her kelimeye  ayrı ayrı ulaşabiliriz

'''print(message[0])  ''' # 0. indexe ulaştık ve terminalde 'Hello' ya karşılık geliyor yani ilk kelime
'''print(message[2]) '''  # 'My' kelimesine karşılık geldi terminalde


#ayrı olarak gelen bilgileri birleştirelim 
message = ' '.join(message)    #ayrı olan kodu tekrar birleştiriyor aralarına boşluk koyarak çünkü ' ' arasına boşluk koyduk 
                               # '' arasına ne koyarsak onunla birleştiriyor tüm kelimeleri otomatik

# Mehmet bilgisinin cümle içinde olup olmadığını kontrol edelim mesela

index = message.find('mehmet')   # mehmet bilgisini arıyor ve kaçıncı karakterde (index) te olduğunu buluyor
print(index)

isFound = message.startswith('H') # içine yazdığımız harfle baslayan bir cümle var mı diyoruz
print(isFound) 

isFound = message.endswith('m')  # m ile biten cümle var mı diyor
print(isFound)

message = message.replace('mehmet','fatih')   # Mehmet bilgisini Fatihle değiştirir
print(message)

#şunu da yapabilirsin
#message = message.replace('öge1','öge2')
#                 .replace('öge3','öge4')
#                 .replace('öge5','öge6')

# mesajın güncel hali : Hello there. my name is fatih selim

message = message.center(100)   # verdiğimiz string bilgimizi 100 karakterlik bir bilgi içerisine alır
print(message)                  # strinki ortalar ve stringden baska 100 ün içinden baska karakter olmadığından kenarlara boşluk konteynırı gibi dağıtır . cümlemiz ortalanır


''' daha fazla python string metodu/kodu için  : https://www.w3schools.com/python/python_ref_string.asp '''
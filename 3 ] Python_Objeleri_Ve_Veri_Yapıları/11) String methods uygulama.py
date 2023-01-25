website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Programlama Rehberiniz (40 saat)"

# 1- ' Hello World ' karakter dizisinin baş ve sondaki boşluk karakterlerini silin.
message = ' Hello World '.strip()
print(message)
# 2- 'www.sadikturan.com' içindeki sadikturan bilgisi haricindeki her karakteri silin
website = website.lstrip('/:pth')           # (sol tarafından ) silmek istediklerimizi attık
website = website.strip('w.moc')            # (tamamından ) silmek istediğimiz karakterleri içine atıyoruz
             #strip() tamamından
             #lstrip() left solundan 
             #rstrip() right sağından sileceklerimiz için kod
print(website)
# 3- 'course' karakter dizisinin tüm karakterlerini küçük harf yapın.
course = course.lower()
print(course)
# 4- 'website' içinde kaç tane a karakteri vardır ? (count('a))

print(website.count(''))
            # website.count('a')      a sayısını hesaplar
            # website.count('www')    www sayısını hesaplar 
            # website.count('www',0,10)  0. indexten 10. indexe kadar arar ve sayar varsa soyler

'''website ı yeniden tanımlayacağız çok değişti :D'''
website = "http://www.sadikturan.com"

# 5- 'website' "www" ile baslayıp "com" ile bitiyor mu?
isFound = website.startswith('www')    
isFound = website.endswith('com')   
print(isFound)    

'''nolur nolmaz diye tekrar tanımlayalım course'u :)'''
course = "Python Kursu: Baştan Sona Programlama Rehberiniz (40 saat)"

# 6- 'website' içinde '.com' ifadesi var mı?
elcevap = website.find('.com')
print(elcevap)

'''hocanın cevabı aşağıda alternatifleriyle'''
result = website.find('com')     # esas cevap : hangi indexte olduğunu soylüyor
result = website.find('com',0,10) # 0 la 10. index aralığını arar bulamazsa -1 değeri verir
cevap1 = course.find('Python') # soldan hangi indexte olduğunu buldu 0 dedi
cevap2 = course.rfind('Python') #sağdan hangi indexte ...(bu nedense sıfır diyo nedenini anlamadım)
print(cevap1)
print(cevap2)
result = website.index('com')  # indeks numarasını arar bulur 
print(result)
result = website.rindex('com')   # sağdan baslar index numarasını söyler
print(result)

''' find ile index metodu arası fark şu find metodu bulamazsa -1 verir terminalde . index ise hata verir'''


# 7- 'course' içindeki karakterlerin hepsi alfabetik mi? (isalpha, isdigit)

result1 = course.isdigit()      # sadece sayılardan mı oluşuyor
result2 = course.isalpha()      # sadece alfabedeki harflerden mi oluşuyor
print(f'alfabetik mi? {result1} numaralardan mı oluşuyor? {result2}')


# 8- 'Contents' ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz

ifade = 'contents'.center(50, '*')        # boşluklara da yıldız ekledik
print(ifade) 
ifade = 'contents'.rjust(50,'*')      # sadece sağ tarafa yıldız ekler
print(ifade)
ifade = 'contents'.ljust(50,'*')            # sadece sol tarafa yıldız ekler
print(ifade)

# 9- 'course' karakter dizisindeki tüm boşluk karakterlerini '-' ile değiştirin.
course = "Python Kursu: Baştan Sona Programlama Rehberiniz (40 saat)"

result = course.replace(' ','-')
print(result)

# 10- 'Hello World' karakter dizisinin 'World' ifadesini 'There' olarak değiştirin.

onemsizKelime = 'Hello World'.replace('World','There')
print(onemsizKelime)

# 11- 'course' karakter dizisini boşluk karakterlerinden ayırın
course = "Python Kursu: Baştan Sona Programlama Rehberiniz (40 saat)"

result = course.split(' ')
print(result)

result = result[2]    # ayırma kodu ile result yukarıda course'un ayrılmış hali olarak tanımlandı burada da course un 2. kelimesine ulaşıyoruz not: 0. kelimeden baslıyor
print(result)


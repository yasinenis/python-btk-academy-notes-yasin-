# dünyanın sonuna doğmuşum ya da ölmüşüm de haberim 

# for ve while 'ye alternatif olarak kullanabileceğimiz...

for x in range(10):
    print(x)             # 0'dan 9'a kadar olan sayılar ekrana yazdırılır

# daha kolay bir yöntemi ise...


numbers = [x for x in range(10)]  # sıfırdan 10 a kadar olan sayıları range içerisinden for döngüsüyle alıyoruz teker teker
# x in içine atıyoruz ve bir x değeri elde ediyoruz ve bunları numbers içersine dizi olarak atıyoruz
print(numbers)

''' 
for 'dan önceki x ' in amacı :
for döngüsünden aldığımız değeri o listenin içinde kullanıyoruz demek

bknz: 36. satirdaki gibi seyler için de kullanılabilir
'''

# bu sekilde de yazılabilir

numbers = []
for x in range(10):
        numbers.append(x)
                                # range ' in otomatik oluşturduğu listeyi
print(numbers)                  # append methodu ile numbers listesine ekledik
                                # listeyi yazdırdık


for x in range(10):
    print(x**2)              # her bir değerin karesi geldi (liste içinde değil)


numbers = [x**2 for x in range(10)]  # yukarıdakinin liste içine alınmış hali
print(numbers)                      

numbers = [x*x for x in range(10) if x%3==0 ] # 3'e bölünenleri sadece yazsın diye if ekleyip x mod 3 yaptık.
print(numbers)                                # ayrıca x*x ile her bir karakterin karesini almış olduk

# numara değilde string ifade yapıyoruz bu sefer

myString = 'Hello'
myList = []

for letter in myString:
     myList.append(letter)
print(myList)

# kısayol olarak şöyle yapabiliriz

myList = [letter for letter in myString]
print(myList)

# bir örnek daha yapalım
years = [1983, 1999, 2008, 1956, 1986] # rastgele doğum tarihleri
# her bir değere tek tek ulaşıp yaş bilgisi hesaplatabiliriz
ages = [2023 - year for year in years]
print(ages)    

# bir örnek daha

result = [x if x%2==0 else 'TEK' for x in range(1, 10)]
print(result) # range metodu 1 den 10 a kadar x e tanımlayacak sayıları ama...
# listenin içine alırken 2 ile tam bölünenleri sayı olarak yazacak ama 
# diğer sayılar yerine TEK yazısını koyacak.


# peki iç içe iki tane döngümüz varsa ne olacak.
result = []
for x in range(3):          # 0'dan 3'e kadar x e tanımladı
    for y in range(3):      # 0'dan 3'e kadar y ye tanımladı
         result.append((x,y))   

print(result)

# yukarıdaki daha basit bir şekilde nasıl yapılabilir

numbers = [(x,y) for x in range(3) for y in range(3)]
print(numbers)



# an itibari ile bu dersleri hangi performans ile ne zaman bitirebileceğim
ders = 176 + 7
print(f"1 ayda bitmesi için günde {ders/30} tane bitmeli")
print(f"2 ayda bitmesi için günde {ders/60} tane bitmeli")
print(f"3 ayda bitmesi için günde {ders/90} tane bitmeli")
result = 3
print(result)






###                   Lists Uygulama Test                   ###



# 1- "BMW, Mercedes, Opel, Mazda" elemanlarına sahip bir liste oluşturunuz.

arabalar = ['BMW','Mercedes','Opel','Mazda']
print(arabalar)

# 2- Liste Kaç elemanlıdır?

result = len(arabalar)
print(result)

# 3- Listenin ilk ve son elemanı nedir?

result = arabalar[0]       #ilk değere baktık
result = arabalar[3]       #son değere baktık
result = arabalar[-1]      # bir de sağdan son değere baktık . sağdan 0 dan baslamaz -1 den baslar. yani sağdan ilk indekse bakmıs olduk
# 4- Mazda değerini Toyota ile değiştirin.

arabalar[3] = 'Toyota' # replace bu tip listelerde kullanılmadığından bu sekil bişey yaptık . anlamı : arabalar adlı listenin 3. indeksini toyota olarak tanımla
print(arabalar)        # bu sayede değiştirmiş olduk bir anlamda da 

'''yeniden tanımlayalım da değiştirdik çünkü'''

arabalar = ['BMW','Mercedes','Opel','Mazda']  

# 5- Mercedes listenin bir elemanı mıdır?

result = 'Mercedes' in arabalar  # in komutu ile içinde olup olmadığını true / false seklinde verir
print(result)

# 6- Listenin -2 indeksindeki değer nedir?

result = arabalar[-2]  # bir listenin ya tanımlı her hangi bir string ifadede de çalışır sanırım :))
print(result)

# 7- Listenin ilk 3 elemanını alın. (ALTERNATİFLER VAR Hocanın)

result = arabalar[0]  + arabalar[1] + arabalar[2]
print(result)
'''         alternatif_1          '''
result = arabalar[0:3]         # 0 dan 3 e kadar al anlamına gelir
print(result)
'''         alternatif_1          '''
result = arabalar[:3]          # hepsini al 3 e kadar anlamındadır
print(result)

# 8- Listenin son 2 elemanı yerine "Toyota" ve "Renault" değerlerini ekleyin.
'''yeniden tanımlayalım da değiştirdik çünkü'''

arabalar = ['BMW','Mercedes','Opel','Mazda']  

arabalar[2:] = 'Toyota','Renault'
print(arabalar)

'''     hocanın yaptiği   '''
arabalar[-2:] = ['Toyota','Renault']
result = arabalar

# 9- Listenin üzerine "Audi" ve "Nissan" değerlerini ekleyin.

arabalar[4:5] = 'Audi','Nissan'
print(arabalar)

'''        hoca        '''
result = arabalar + ['Audi','Nissan']

# 10- Listenin son elemanını silin.

del arabalar[-1]          # del komutu siliyormuş demekki
print(arabalar)

# 11- Liste elemanlarını tersten yazdırınız.

result = arabalar[::-1]    # tamamına birer birer git ama -1 er olursa tersten gider

# 12- Aşağıdaki verileri bir liste içinde saklayınız.

    # studentA: Yiğit Bilgi 2010, (70,60,70)
    # studentB: Sena Turan 1999, (80,80,70)
    # studentC: Ahmet Turan 1998, (80,70,90)

studentA = ['Yiğit','Bilgi',2010,[70,60,70]]
studentB = ['Sena','Turan',1999,[80,80,70]]
studentC = ['Ahmet','Turan',1998,[80,70,90]]

# 13- Liste elemanlarınızı ekrana yazdırınız.

result = studentA[0]    # Yiğit bilgisine karşılık gelicektir

result = studentB[1]    # Turan bilgisine karşılık gelecektir

result = studentC[3]    # student C nin not listesi gelir

'''listenin içinden baska bir listeye geçmek için'''
result = studentC[3][0]  # studentC listesinin 3. indeksindeki not listesinin ilk indeksindeki 80 i verir
print(result)

'''Yiğit Bilgi dokuz yaşinda ve not ortalamasi şudur şeklinde yazalim'''
result = f"{studentA[0]} {studentA[1]} {2023-studentA[2]} yasinda ve not ortalamasi {(studentA[3][0]+studentA[3][1]+studentA[3][2]) /3}"
print(result)
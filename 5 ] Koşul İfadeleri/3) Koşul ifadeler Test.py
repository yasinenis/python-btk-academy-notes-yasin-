####                      Test Uygulama                      ####             

# 1- Kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyet alabilme 
# durumunu kontrol ediniz. Ehliyet alma koşulu en az 18 ve eğitim durumu 
# lise ya da üniversite olmalıdır.

isim = input('İsim : ')
yas = int(input('Yaş: '))
eğitim = input('Eğitiminiz: ')

if ( yas > 18 ):
    if ( eğitim == 'üniversite' ) or ( eğitim == 'lise' ):
        print('Ehliyet alabilirsiniz :) ')
else:
    print('Ehliyet alamaya uygun değilsiniz :( ') 

# 2- Bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplanan ortalamaya göre 
#    not aralığına karşılık gelen not bilgisini yazdırınız.
#    0 - 24  => 0
#    25 - 44  => 1 
#    45 - 54  => 2
#    55 - 69  => 3
#    70 - 84  => 4
#    85 - 100  => 5

yazili1 = float(input('İlk Sınav: '))
yazili2 = float(input('İkinci Sınav: '))
sözlü = float(input('Sözlü: '))

ort = (yazili1 + yazili2 + sözlü) / 3

if (0 <= ort <= 24 ):
    print('NOT: 0 ')
elif (25 <= ort <= 44 ):
    print('NOT: 1')
elif (45 <= ort <= 54 ):
    print('NOT: 2')
elif (55 <= ort <= 69 ):
    print('NOT: 3')
elif (70 <= ort <= 84 ):
    print('NOT: 4')
elif (85 <= ort <= 100 ):
    print('NOT: 5')

# 3- Trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki bilgilere
#    göre hesaplayınız..
#    1. Bakım => 1. yıl
#    2. Bakım => 2. yıl
#    3. Bakım => 3. yıl
#    *** Süre hesabını alınan gün, ay, yıl bilgisine göre gün bazlı hesaplayınız
#    (şimdi) - (2018/8/1) ==> gün

days = int(input('Aracınız kaç gündür trafikte: '))

if (days <= 365):
    print('1.servis aralığı')
elif days > 365 and days <= 365*2:
    print('2.servis aralığı')
elif days > 365*2 and days<=365*3:
    print('3.servis aralığı')
else:
    print('hatalı süre girdiniz')

# date time modülü kullanarak cevaplayalım
import datetime
tarih = (input('aracınız hangi tarihte trafiğe çıktı (2019/8/9) '))
tarih = tarih.split('/')          # split metoduyla tarih bilgisini slash işaretinden ayırdık
trafigeCikis = datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2])) # trafiğe çıkış isimli date.time objesi hazırlamıs olduk
simdi = datetime.datetime.now()   # bugünün tarihini almış oluyoruz date time objesi olarak alıyoruz aynı zamanda
fark = simdi - trafigeCikis 
days = fark.days   # fark tanımının içinde ggün ve saat falan vardı biz fark tanımından günleri alıp tanımladık sadece bunun sayesinde 
print(simdi)

if (days <= 365):
    print('1.servis aralığı')
elif days > 365 and days <= 365*2:
    print('2.servis aralığı')
elif days > 365*2 and days<=365*3:
    print('3.servis aralığı')
else:
    print('hatalı süre girdiniz')
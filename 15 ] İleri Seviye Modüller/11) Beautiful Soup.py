html_doc = """
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>İlk web sayfam</title>
</head>
<body>
    <h1 id="header">    
        <!--ben bu h1 etiketine renk falan v.b vermek istesem bu header keywordünü kullanıcam-->
        Sen buralara nirden geldin :D
    </h1>

    <div class="grup1">
        <h2>
            Programlama
        </h2>


        <ul>
            <li>Menü 1</li>
            <li>Menü 2</li>
            <li>Menü 3</li>
        </ul>
    </div>

    <!--grubu kopyaladık aşağıyada-->

    <div class="grup2">
        <h2>
            Modüller
        </h2>


        <ul>
            <li>Menü 1</li>
            <li>Menü 2</li>
            <li>Menü 3</li>
        </ul>
    </div>

    <div class="grup3">
        <h2>
            Django
        </h2>


        <ul>
            <li>Menü 1</li>
            <li>Menü 2</li>
            <li>Menü 3</li>
        </ul>
    </div>

<!--             resim nasıl konur?                        -->

    <img src="brain.png" alt="">

    <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
    <a class="sister" href="http://example.com/elsie" id="link2">Elsie</a>
    <a class="sister" href="http://example.com/elsie" id="link3">Elsie</a>

</body>
</html>

<!-- div: grubu temsil eder . isim verilebilir-->

"""


from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc, 'html.parser') 
# beautiful soup bu verdiğimiz dökümanı pars (analiz) edicek ve analiz
# işleminde nasıl bir parser (denetleme mekanizması) kuracak onu da ikinci
# parametrede belirtiyoruz.
print("___________________(1)_______🐛____________ prettify ________________")
result = soup.prettify()
# BeautifulSoup üzerinden prettify yi çalıştırdığımızda bize (kod hafif bozuksa falan) düzeltilmiş düzgün bir şekilde verecek
print(result)
print("____________________(2)______🐛____________________________")
# web sitesinden başlığı almaya çalışalım ⇲
result = soup.title
print(result)
print("__________________(3)________🐛___________________________")
# "     "   head kısmını alalım ⇲
result = soup.head
print(result)
print("__________________4________🐛____________________________")
# "     "   body etiketini alalım ⇲
result = soup.body
print(result)



                # ETİKET KISMI HARİCİ İÇTEKİ BİLGİLERİ ALALIM BU SEFER



print("__________________5________🐛____________________________")
result = soup.title.name    # etiket ismi geldi sadece
print(result)
print("___________________6_______🐛____________________________")
result = soup.title.string  # bu sefer içteki bilgi sadece geldi.
print(result)
print("_________________7_________🐛____________________________")
result = soup.h1    # h1 içindeki bilgilerle gelir . gördük yukarda bunu zaten
print(result)
print("__________________8________🐛____________________________")
# iki tane h2 var ise hangisini getirir
result = soup.h2
print(result)   # ilk h2 yi getirdi
print("_________________9_________🐛____________________________")
# h2 nin de name ini alalım
result = soup.h2.name
print(result)   # h2 dedi sadece (etiket ismi)(yukarda öğrenmiştik)
print("_____________________10_____🐛____________________________")
# içindeki bilgiyi alalım
result = soup.h2.string
print(result)
print("_____________________11_____🐛____________________________")
result = soup.find_all('h2')
print(result)
print("____________________12______🐛____________________________")
# find_all özelliği
result = soup.find_all('h2')    # sayfada bulduğu tüm h2 etiketlerini bize getir demek.
print(result) # liste şeklinde verdi
print("____________________13______🐛____________________________")
result = soup.find_all('h2')[0] # listenin ilk h2 sini verir
print(result)
print("___________________14_______🐛____________________________")
result = soup.find_all('h2')[1] # listenin sadece ikinci elemanını verir
print(result)
print("___________________15_______🐛____________________________")
result = soup.div
print(result)   # sayfadaki ilk div getirilir
print("__________________16________🐛____________________________")
# hangi div gelsin istersem o gelsin diye şu⇲
result = soup.find_all('div')[1]   # divlerin tüm hepsini buluruz liste halinde elimize gelir içinden index yardımı ile istediğimiz bir divi seçeriz.
print(result)   # birinci indexteki div geldi
print("___________________________🐛____________________________")
# div grup 2 nin altındaki ul etiketine ulaşalım(yaptık daha önce)
result = soup.find_all('div')[1].ul
print(result)
print("__________________17________🐛____________________________")
# div grup 2 nin altındaki ul ordanda li ye ulaşalım
result = soup.find_all('div')[1].ul.li  
print(result)   # index vermeyince ilk li yi verdi
print("___________________18_______🐛____________________________")
# bu sefer li lerin hepsi gelsin istiyorsak
result = soup.find_all('div')[1].ul.find_all('li')
# find all metodunu tekrar kullanabiliriz
print(result) # liste halinde geldi
print("___________________19_______🐛____________________________")
result = soup.div.findChildren()    #not grup-1 divi
print(result)   # div altındaki bütün alt elemanlar (childrenlar) getirilecek
print("___________________20_______🐛____________________________")
# bir sonraki dive geçelim(grup 2 ye)
result = soup.div.findNextSibling() # bir sonrakine geçiyor
print(result)
print("____________________21______🐛____________________________")
# tekrar findNextSibling() kullanırsak bir diğerine geçer
result = soup.div.findNextSibling().findNextSibling()
print(result)
print("____________________22______🐛____________________________")
# ardından bir öncekine geçmek istersek?     findPrevious()
result = soup.div.findNextSibling().findNextSibling().findPreviousSibling()
print(result)
print("____________________ 23 ______🐛____________________________")
# 60 - 62. satırlar arası eklediğimiz a etiketlerindeki linkleri alalım
result = soup.find_all('a')
print(result)
print("____________________(24)______🐛____________________________")
# yukarıdaki aldığımız a etiketlerinin üzerinde dolaşalım for ile
for link in result:
    print(link)
print("____________________(25)______🐛____________________________")
# a etiketlerinin sadece iç kısımları gelsin
for link in result:
    print(link.get('href'))# get ile almak istediğimiz attribute özelliğini veriyoruz
print("__________________________🐛____________________________")

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

</body>
</html>

<!-- div: grubu temsil eder . isim verilebilir-->

"""


from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc, 'html.parser') 
# beautiful soup bu verdiğimiz dökümanı pars (analiz) edicek ve analiz
# işleminde nasıl bir parser (denetleme mekanizması) kuracak onu da ikinci
# parametrede belirtiyoruz.
print("___________________________🐛____________________________")
result = soup.prettify()
# BeautifulSoup üzerinden prettify yi çalıştırdığımızda bize (kod hafif bozuksa falan) düzeltilmiş düzgün bir şekilde verecek
print(result)
print("___________________________🐛____________________________")
# web sitesinden başlığı almaya çalışalım ⇲
result = soup.title
print(result)
print("___________________________🐛____________________________")
# "     "   head kısmını alalım ⇲
result = soup.head
print(result)
print("___________________________🐛____________________________")
# "     "   body etiketini alalım ⇲
result = soup.body
print(result)
                # ETİKET KISMI HARİCİ İÇTEKİ BİLGİLERİ ALALIM BU SEFER
print("___________________________🐛____________________________")
result = soup.title.name    # etiket ismi geldi sadece
print(result)
print("___________________________🐛____________________________")
result = soup.title.string  # bu sefer içteki bilgi sadece geldi.
print(result)
print("___________________________🐛____________________________")
result = soup.h1    # h1 içindeki bilgilerle gelir . gördük yukarda bunu zaten
print(result)
print("___________________________🐛____________________________")
# iki tane h2 var ise hangisini getirir
result = soup.h2
print(result)   # ilk h2 yi getirdi
print("___________________________🐛____________________________")
# h2 nin de name ini alalım
result = soup.h2.name
print(result)   # h2 dedi sadece (etiket ismi)(yukarda öğrenmiştik)
print("___________________________🐛____________________________")
# içindeki bilgiyi alalım
result = soup.h2.string
print(result)
print("___________________________🐛____________________________")
result = soup.find_all('h2')
print(result)
print("___________________________🐛____________________________")
# find_all özelliği
result = soup.find_all('h2')    # sayfada bulduğu tüm h2 etiketlerini bize getir demek.
print(result) # liste şeklinde verdi
print("___________________________🐛____________________________")
result = soup.find_all('h2')[0] # listenin ilk h2 sini verir
print(result)
print("___________________________🐛____________________________")
result = soup.find_all('h2')[1] # listenin sadece ikinci elemanını verir
print(result)
print("___________________________🐛____________________________")
result = soup.div
print(result)   # sayfadaki ilk div getirilir
print("___________________________🐛____________________________")
# hangi div gelsin istersem o gelsin diye şu⇲
result = soup.find_all('div')[1]   # divlerin tüm hepsini buluruz liste halinde elimize gelir içinden index yardımı ile istediğimiz bir divi seçeriz.
print(result)   # birinci indexteki div geldi
print("___________________________🐛____________________________")
# div grup 2 nin altındaki ul etiketine ulaşalım(yaptık daha önce)
result = soup.find_all('div')[1].ul
print(result)
print("___________________________🐛____________________________")
# div grup 2 nin altındaki ul ordanda li ye ulaşalım
result = soup.find_all('div')[1].ul.li  
print(result)   # index vermeyince ilk li yi verdi
print("___________________________🐛____________________________")
# bu sefer li lerin hepsi gelsin istiyorsak
result = soup.find_all('div')[1].ul.find_all('li')
# find all metodunu tekrar kullanabiliriz
print(result) # liste halinde geldi
print("___________________________🐛____________________________")
result = soup.div.findChildren()    #not grup-1 divi
print(result)   # div altındaki bütün alt elemanlar (childrenlar) getirilecek
print("___________________________🐛____________________________")
# bir sonraki dive geçelim(grup 2 ye)
result = soup.div.findNextSibling() # bir sonrakine geçiyor
print(result)
print("___________________________🐛____________________________")
# tekrar findNextSibling() kullanırsak bir diğerine geçer
result = soup.div.findNextSibling().findNextSibling()
print(result)
print("___________________________🐛____________________________")
# bir öncekine geçmek istersek?     findPrevious()
result = soup.div.findNextSibling().findNextSibling().findPreviousSibling()
print(result)
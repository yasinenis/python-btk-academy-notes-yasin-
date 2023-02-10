name = 'Sadık Turan'

for letter in name:
    if letter == 'a':
        break             # break : kelimede a harfini görürse durdurur
    elif letter == 'ı':
        continue          # continue : kelimede ı harfini atlar devam eder (ı harfinin olduğu döngü
                          # turunu iptal eder kaldığı yerden devam eder)   
    print(letter)

#------------------------------------------
# peki while döngüsünde kullanırsak continue 'i :

x = 0
while x < 5:
    x += 1         
    if x == 2:
        break            # while döngüsünden çıkmamızı sağlar . 2 gelince 
    print(x)


x = 0
while x < 5:
    x += 1          # x += 1 'i döngünün basında koyduk çünkü contuine komutundan aşağısı devam etmez x 2 de takılı kalır
    if x == 2:
        continue   # o anki döngüyü iptal eder başa döner . altındaki kısım devam etmeyeceği için
    print(x)       #     x 'i bir artırma kısmını yukarıya koyduk


#------------------------------------------
#                                TEST


# 1- 100 e kadar tek sayıların toplamı

x = 1
result = 0

while x <= 100:
    x += 1
    if x % 2 == 0:
        continue
    result += x
    

print(f'toplam : {result} ')


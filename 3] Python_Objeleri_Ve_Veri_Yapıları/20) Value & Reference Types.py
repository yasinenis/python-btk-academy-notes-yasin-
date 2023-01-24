# bir veri/obje tanımladığımızda bilgisayar belleğinde nasıl değerlendiriliyor

x = 5
y = 25

x = y  # x burda 25 , y burda 25 olmuş oldu

y = 10  # y 10 oldu ama x 25 olarak kaldı

print(x,y)

# y 'de yaptığımız güncelleme x 'i etkiler mi buna baktık (etkilenmedi)

# string, number(float/int) => value types altında ele alınır
# value types => string, number(float/int)
''' value typei lerde y'de yaptiğimiz güncelleme x 'i etkilemiyor'''

# reference types => list,class
a = ["apple","banana"]
b = ["apple","banana"]

a = b

b[0] = "grape"

print(a, b)

'''reference types lerde b 'ye yaptiğimiz güncelleme a 'yi etkiliyor '''


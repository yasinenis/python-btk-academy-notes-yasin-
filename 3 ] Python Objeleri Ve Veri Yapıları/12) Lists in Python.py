###                   Lists In Python                   ###    

message = 'Hello There. My name is Sadık Turan'
print(message[0])     # 0. indeksteki 'H' harfini yazdırır

message = 'Hello There. My name is Sadık Turan'.split()
print(message[0])     # 0. indeksteki 'Hello' kelimesin yazdırır
                      # çünkü split kelime olarak ayırdı ve kelimelere index verdi
# ------------------------------------------------------

my_list = [1,2,3]
my_list = ['bir',2, True, 5.6]
print(my_list)
# ------------------------------------------------------

list1 = ['one','two','three']
list2 = ['four','five','six']

numbers = list1 + list2     # topladık içindekileri terminal yan yana koydu
print(numbers)

print(len(numbers))
# ------------------------------------------------------

userA = ['Sadık', 36]
userB = ['Çınar',  2]

users = userA + userB

print(users)

#

userA = ['Sadık', 36]
userB = ['Çınar',  2]

users = [userA, userB]      #liste içinde liste yapmak için buna çevirdik yukardaki ifadeyi

print(users)

# yukardaki bilgilere ulaşmak için ne yapabiliriz

print(users[1])         # liste elemanının 1. indexini verdi (0. index değil) 

print(users[0][1])     # Sadık bilgisi 0. indekin 0.indeksinde
                       # 36 bilgisi 0. indeksin 1. indeksinde (terminal bunu yazacak)
                       # Çınar bilgisi 1. indeksin 0. indeksinde
                       # 2 bilgisi 1. indeksin 1. indeksinde
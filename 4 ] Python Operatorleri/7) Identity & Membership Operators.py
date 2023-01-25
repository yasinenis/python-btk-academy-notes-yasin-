#####          Identity Operator: is      #####

x = y = [1, 2, 3]
z = [1, 2, 3]

print(x==y)
print(x==z) # True dedi çünkü eşitlik operatorü listelere atılan değerlerin karşılaştırması yapılır

print(x is y)   # True der adresi falan da aynı mı her seyi diyor sanırım is de
print(x is z)   # False dedi çünkü: x ve z nin farklı bir referansa sahip old. biliyoruz
# listelerin aynı değere sahip olması bile false demekten alıkoymadı is komutu için
# is 'de tanımlanan objelerin aynı lup olmadığını (aynı adresi tutup tutmadığı) kontrol ediyor. içindeki değerler aynı olsa bile farklı objelerse false der

x = [1, 2, 3]
y = [2, 4]

print(x is y)  # False der 

del x[2]    # y 'ye benzetmek için x 'in 2. indexindeki 3 sayısını sildik
y[1] = 1    # 1. indexe 1 ekledik
y.reverse() # y 'yi ters çevirdik
            # x ve y 'nin içini aynı yaptık

print(x==y)     # True der içini kontrol ediyor == operatoru
print(x is y)   # x bi y objesi midir değil o ayrı bir obje o nedenle False dedi



####         Membership Operator: in      #####

x = ['apple','banana']
print('banana' in x)     # x 'in içinde banana var mı demek . True verir

name = 'Çınar'
print('a' in name)  # True der
print('a' not in name) # False der (not var dikkat tam tersi cevap getirir)
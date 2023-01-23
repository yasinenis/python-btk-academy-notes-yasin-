name = 'Selim'
surname = 'Turan'
age = 22

greeting = 'My name is' + ' ' + name + ' and \nI am ' + str(age) + ' years old' # \n işareti alt satıra yaz demek
print(greeting)

print(greeting[0])    

print(len(greeting))  #kaç karakterli olduğunu hesapladık

print(greeting[38]) #38.sırada hangi karakter var onu bulduk (ilk sıra 1 den değil 0 dan baslıyor aklında olsun)

lenght = len(greeting)

print(greeting[lenght-1]) #lenght'in yani (uzunluu) kaç karakter olduğunu 39 bulduk . 0 dan basladığı için -1 dedik

#veya bu kadar uzatmak yerine aşağıdaki de iş görür
print(greeting[-1]) 

print(greeting)

print(greeting[2:5])   #ikinci index numarasından basla 5. karaktere kadar git demek

print(greeting[3:])    #3 ten baslar sonuna kadar gider

print(greeting[:16])   #bastan baslar 16. karaktere kadar gider

print(greeting[2:40:3]) # 2 den basla 40 a kadar git ama her karakteri alma üçer üçer al

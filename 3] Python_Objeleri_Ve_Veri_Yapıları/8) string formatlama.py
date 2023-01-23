# {} .format() 

name = 'Melina'
surname = 'Babayeva'
age =37
print('My name is {} {}'.format(name, surname))  #formatın içine yazdığımızı süslü parantezlere yazıyor
#otomatik ilk parntez sıfır ikincisi birinciyi içine alacak diye tanımlanmıstır
#eğer numaralandırırsak tam tersi yapabiliriz anladin sen oni
print('My name is {1} {0}'.format(name, surname))

#terminalde bu sefer name sonda surname basta yazmış olur

print('My name is {s} {n}'.format(n=name, s=surname)) #bu sekilde d eyapılabilir

#pekiştirecek başka bir örnek

print('My name is {} {} and Im {} years old.'.format(name, surname , age))

#-----------------------------------------

result = 200 / 700
print('the result is {}'.format(result))
#bunu değiştirelim
print('the result is {r:1.3}'.format(r=result))
#format içinde resultu r diye tanımladık ki süslü parantez içinde resultu floatdan int'e çrvirelim
# {r:1.3} deki 3 virgülden sonra kaç basamak olcağını tmsil ediyor 
# {r:1.3} deki 1 ise tam kısım için kaç alan boşluk bırakmak gerektiğini hesaplıyor

#-----------------------------------------

# f String

print(f"My name is {name} {surname} and I'm {age} years old.")

#basına f koyarsan süslü parantezlere direk tanımlamaları yerlestir 
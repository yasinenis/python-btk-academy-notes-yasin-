website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

# 1 - 'course' karakter dizisinde kaç karakter blunmaktadır ?

print('---1')
print(len(course))          # len() kullandık

# 2 - 'website' içinden www karakterlerini alın.

print('---2')
print(website[7:10])

# 3 - 'website' içinden com karakterlerini alın.

print('---3')
print(website[22:25])

# 4 - 'course' içinden ilk 15 ve son 15 karakterlerini alın.
lenght = len(course)
print('---4.1')
print(course[0:15])
print('---4.2')
print(course[-15:lenght])

# 5 - 'course' ifadesindeki karakterleri tersten yazdırın.

print('---5')
print(course[::-1])                          # N O T [::] isareti tamamını yazar  [::-1] tamamını tersten yazar

name, surname, age, job = 'Bora', 'Yılmaz', 32, 'mühendis'

# 6 - Yukarıda verilen değişkenler ile ekrana aşağıdaki ifadeyi yazdırın.
#      'Benim adım Bora Yılmaz, Yaşım 32 ve mesleğim mühendis

print('---6')
print(f'Benim adım {name} {surname} , yaşım {age} ve mesleğim {job}')

# 7 - 'Hello world' ifadesindeki w harfini 'W' ile değiştirin.

a = 'Hello world'
a = a[0:6] + 'W' + a[-4:]

print(a)

# 8 - 'abc' ifadesini yan yana 3 defa yazdırın

a = 'abc' 
print(a * 3)
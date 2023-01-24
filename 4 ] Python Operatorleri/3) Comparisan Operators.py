# Comparisan = karşılaştırma 
# yazdığımız uygulamalarda programın gidişatının belli koşullar altında farklı yollara gitmesini sağlamak istersek karşılaştırma operatorlerini kullanmamız gerek.

# username, password => database'e gider
# 'sadikturan' , '123456'

# data base den gelen ve kullanıcının girdiği username password uyuşması lazım

a, b, c, d = 5, 5, 10, 4

result = a==b              # a, b 'ye eşit mi? demek

print(result)   # a , b 'ye eşit olduğu için cevap True

result = (a == c)   # istersen paranteze de alabilirsin
print(result)

password = '1234'
username = 'sadikturan'

result = ('sdktrn'== username)   # false der
result = ('sadikturan' == username) #True der
result = (a != b)     ###  Eşit değil mi demek. != işareti   Fase der terminal
result = (a != c)
result = (a > c)   # false der
result = (a < c)   # true der
result = (a >= b)     ### a büyüktür aynı zamanda eşit midir? c 'ye der . # True der terminal
result = (a <= b)     ### a küçük/eşit midir b ye?
result = (True == 1)  # True numerik olarak 0 'a eşittir
result = (False == 0) # False numerik olarak 0 'a eşittir
result = False+ True + 40  # yani numerik olarak işlemlere de katabiliyoruz



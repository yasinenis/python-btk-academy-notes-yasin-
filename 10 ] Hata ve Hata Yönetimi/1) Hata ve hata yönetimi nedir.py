# error (hata)

# error handling ( hata yönetimi )

# bu derste öğreneceklerimiz
        # hata nedir
        # hata türleri
        # hatalara nasıl önlem alırız (bir sonraki ders)


        # VALUE ERROR
# kullanıcıdan number istiyorsak ve kullanıcı string ifade yazması.
int('1a2')
        # ValueError: invalid literal for int() with base 10: '1a2'



        # NAME ERROR    
# daha önce tanımlamadığınız bir değişkeni ekrana yazdırmaya çalışmak.
print(a)
       # NameError: name 'a' is not defined

        # ZERO DİVİSİON ERROR
# kullanıcı bölme işlemi yaparken ilk girdiği sayı 10 ikincisi 0 ise
print(10/0)
        # ZeroDivisionError: division by zero

        # SYNTAX ERROR
print('denem'e)
        # SyntaxError: invalid syntax
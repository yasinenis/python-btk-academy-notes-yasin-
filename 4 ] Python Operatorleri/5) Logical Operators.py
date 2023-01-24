### Mantıksal operatörler

x = 5
result = 5 < x < 10
print(result)

# bu işlemleri böyle yapmak yerine ; and/or/not opratorlerini kullanabiliriz

             ###### and #####

result = x > 5 and x < 10    # x 5 'ten büyük ve 10 'dan küçük mü??
# and operatorünün sağ ve solundaki değerler ayrı ayrı True ise sonuç True 'dur

#    True, True => True 
#    True, False => False

result = (x > 5) and (x < 10)

# strig ifadelerde de bunu su sekil kullanabiliriz
hak = 5
devam = 'e'
result = (hak > 0) and (devam == 'e')  # hak 0 'dan büyükse ve devam seçeneği eğer e olarak işaretlenmişse

# terminal true der



            ###### or ######

result = (x > 0) or (x % 2 == 0)  # biri doğru olsa yeter
# hatırlatma(!)    (x % 2 == 0) x 'in çift olma durumunu sorguluyor .

# True, False => True
# True, True  => True
# False, False => False


            ##### not ######

# not tam tersini alıyor

result = not(x > 0)

print(result)


import requests
import json

api_url = "https://v6.exchangerate-api.com/v6/(api key buraya yazılmalı)/latest/"

bozulan_doviz = input("bozulan döviz türü: ")
alinan_doviz = input("alınan döviz türü: ")
miktar = int(input(f"Ne kadar {bozulan_doviz} bozdurmak istiyorsun? "))

result = result = requests.get(api_url+bozulan_doviz)   # apideki bilgilere ulaştık
result = json.loads(result.text)    # result.text ile önce stringe texte çevirdik sonra bunu loads a verdik o da bize dict e çevirdi ki içinden lazım olanları seçebilelim.

print("1 {0} = {1} {2}".format(bozulan_doviz, result["conversion_rates"][alinan_doviz], alinan_doviz))
print("{0} {1} = {2} {3}".format(miktar, bozulan_doviz, miktar * result["conversion_rates"][alinan_doviz], alinan_doviz))
print(f"\n döviz kuru son güncellenme tarihi: {result['time_last_update_utc']}")
import requests
from bs4 import BeautifulSoup

url = "https://www.n11.com/bilgisayar/dizustu-bilgisayar"
headers = {
    "User-Agent": "User argent goodle dan sorgulanabilir"
}

icerik = requests.get(url, headers=headers).content

soup = BeautifulSoup(icerik, "html.parser")

list = soup.find_all("li", attrs={"class":"column"})

for li in list:
    name = li.find("h3", attrs={"class":"productName"}).text
    link = li.find("a", attrs={"class":"plink"}).get("href")
    newPrice = li.find("ins").text
    #oldPrice = li.find("span", attrs={"class":"oldPrice noLine cPoint priceEventClick  hidden "}).text
    print(f"name: \n{name} \nlink: \n{link} \nprice: \n{newPrice}\n\n\n")
# sadece old price da hata veriyor
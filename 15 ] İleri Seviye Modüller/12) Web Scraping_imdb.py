import requests
from bs4 import BeautifulSoup


url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
headers = {
    "User-Agent": "burada User-Agent google dan sorgulanabilir"
}

# içeriği al html ye tanımla
html = requests.get(url, headers=headers).content

# içeriği html.pareser e göre ayır soup  a tanımla
soup = BeautifulSoup(html, "html.parser")


movie_list = soup.find("ul", attrs= {"class":"ipc-metadata-list ipc-metadata-list--dividers-between sc-3a353071-0 wTPeg compact-list-view ipc-metadata-list--base"}).find_all("li", limit=20)

count = 1

year = "Year"
rating = "Rating"
title = "    Title"

print(f"{title.ljust(60)} {year.ljust(10)} {rating}")

for movie in movie_list:
    result_title = movie.find("h3", attrs= {"class":"ipc-title__text"}).text
    result_date = movie.find("span", attrs= {"class":"sc-14dd939d-6 kHVqMR cli-title-metadata-item"}).text
    result_rating = movie.find("span", attrs= {"class":"ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating"}).text
    
    
    #print(count,"-", result_date, "  ", result_rating, "  ", result_title)
    print(f"{result_title.ljust(60)} {result_date.ljust(10)} {result_rating}")
    count +=1
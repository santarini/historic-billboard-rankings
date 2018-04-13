import os
import requests
import bs4 as bs
import csv
import re

response = requests.get('https://www.billboard.com/charts/hot-100/1958-08-11')
soup = bs.BeautifulSoup(response.text, 'lxml')
chart = soup.findAll("div", {"class": "container"})[2]
for row in chart.findAll('article'):
    weekRank = row.find("span", {"class": "chart-row__current-week"}).text
    songName = row.find("h2", {"class": "chart-row__song"}).text
    try:
        artistName = row.find("a", {"class": "chart-row__artist"}).text
    except(TypeError, AttributeError):
        artistName = row.find("span", {"class": "chart-row__artist"}).text
    
    print(weekRank+", "+ artistName +" - "+songName)

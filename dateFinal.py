import os
import requests
import bs4 as bs
import csv
import re

i = 1958
dateText = '1958-08-11'
with open('dateRank.csv', 'a') as csvfileB:
    fieldnames = ['Year','IssueDate','Rank', 'Artist', 'Song']
    writer = csv.DictWriter(csvfileB, fieldnames=fieldnames, lineterminator = '\n')
    writer.writeheader()
    #date loop start
    response = requests.get('https://www.billboard.com/charts/hot-100/1958-08-11')
    soup = bs.BeautifulSoup(response.text, 'lxml')
    chart = soup.findAll("div", {"class": "container"})[2]
    for row in chart.findAll('article'):
        weekRank = row.find("span", {"class": "chart-row__current-week"}).text
        songName = row.find("h2", {"class": "chart-row__song"}).text
        try:
            artistName = row.find("a", {"class": "chart-row__artist"}).text
            artistName = artistName.strip()
        except(TypeError, AttributeError):
            artistName = row.find("span", {"class": "chart-row__artist"}).text
            artistName = artistName.strip()

        writer.writerow({'Year': i,'IssueDate':dateText,'Rank':weekRank, 'Artist':artistName,'Song':songName})
        print(weekRank +", " + artistName +" - "+songName)
    ##i+=1


import os
import requests
import bs4 as bs
import csv
import re
import time
start_time = time.time()
with open("billboardDateHrefs.csv") as csvfileA:
    reader = csv.DictReader(csvfileA)
    with open('dateRank.csv', 'a') as csvfileB:
        fieldnames = ['Year','IssueDate','Rank', 'Artist', 'Song']
        writer = csv.DictWriter(csvfileB, fieldnames=fieldnames, lineterminator = '\n')
        for row in reader:
            year = (row['Year'])
            dateText = (row['IssueDate'])
            href = (row['Href'])
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',}
            url = 'https://www.billboard.com' + href
            response = requests.get(url, headers=headers)
            soup = bs.BeautifulSoup(response.text, 'lxml')
            chart = soup.findAll("div", {"class": "container"})[2]
            for row in chart.findAll("article", {"class": "chart-row"}):
                weekRank = row.find("span", {"class": "chart-row__current-week"}).text
                songName = row.find("h2", {"class": "chart-row__song"}).text
                try:
                    artistName = row.find("a", {"class": "chart-row__artist"}).text
                    artistName = artistName.strip()
                except(TypeError, AttributeError):
                    artistName = row.find("span", {"class": "chart-row__artist"}).text
                    artistName = artistName.strip()

                writer.writerow({'Year': year,'IssueDate':dateText,'Rank':weekRank, 'Artist':artistName,'Song':songName})
                print(dateText+", "+ year+": "+weekRank +", " + artistName +" - "+songName)
elapsed_time = time.time() - start_time
print(elapsed_time)

import os
import requests
import bs4 as bs
import csv
import re

i =1958
with open('billboardDateHrefs.csv', 'a') as csvfileB:
    fieldnames = ['Year','IssueDate','Href']
    writer = csv.DictWriter(csvfileB, fieldnames=fieldnames, lineterminator = '\n')
    writer.writeheader()
    while i <=  2018:
        response = requests.get('https://www.billboard.com/archive/charts/'+ str(i) +'/hot-100')
        soup = bs.BeautifulSoup(response.text, 'lxml')
        yearTable = soup.find('tbody')
        for row in yearTable.findAll('tr'):
            dateColumn = row.find('a')
            dateText = dateColumn.text
            hrefStr = dateColumn['href']
            writer.writerow({'Year': i,'IssueDate':dateText,'Href':hrefStr})
            print(str(i) +", "+ dateText +", "+ hrefStr)
        i+=1

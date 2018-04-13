import requests
import bs4 as bs

i =1958
while i <  2018:
    response = requests.get('https://www.billboard.com/archive/charts/'+ str(i) +'/hot-100')
    soup = bs.BeautifulSoup(response.text, 'lxml')
    yearTable = soup.find('tbody')
    for row in yearTable.findAll('tr'):
        dateColumn = row.find('a')
        dateText = dateColumn.text
        hrefStr = dateColumn['href']
        print(dateText)
        print(hrefStr)
    i+=1

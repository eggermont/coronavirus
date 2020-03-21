from bs4 import BeautifulSoup
from urllib.request import urlopen
import time
import pandas as pd

url = 'https://en.m.wikipedia.org/wiki/2019%E2%80%9320_Wuhan_coronavirus_outbreak'
page = urlopen(url).read()
soup = BeautifulSoup(page,'lxml')

project_folder = '/Users/alexiseggermont/Dropbox/01. Personal/04. Models/58. Coronavirus/'

tables = soup.find_all('table')
print(len(tables))

table = tables[2]


table_rows = table.find_all('tr')
fd = open(project_folder+'incidence_data.csv','a')

for tr in table_rows:
    try:
        td = tr.find_all('td')
        row = [tr.text for tr in td]
        print(row)###
        #try:
        timestamp = pd.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        date = pd.datetime.now().strftime("%Y/%m/%d")
        country = row[0].strip().replace(',','').replace('\n','')
        incidence = row[1]
        incidence = incidence.replace(',','').replace('\n','')
        fatalities = row[2]
        fatalities = fatalities.replace(',','').replace('\n','')
        recoveries = row[3]
        recoveries = recoveries.replace(',','').replace('\n','')
        myCsvRow=timestamp+","+date+","+country+","+incidence+","+fatalities+","+recoveries+"\n"
        print(myCsvRow)
        fd.write(myCsvRow)
    except:
        pass
    #except Exception as e:
    #    print(e)
    #    pass
fd.close()



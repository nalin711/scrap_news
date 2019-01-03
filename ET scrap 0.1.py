import requests
from bs4 import BeautifulSoup
import newspaper

# insert epu_classifier

year = 2018 # set starting year for scraping

user = "nalinpriyaranjan"  # set user name here
page_no= 37226
while year <= 2018:
    month = 1           # set month counter
    while page_no <= 43461:
        #download_dir1 = "C:/Users/%s/PycharmProjects/hw/ET_scraped_%s_%s.txt" % (user, year, month) # remane this based on pycharm project directory
        #download_dir2 = "C:/Users/%s/PycharmProjects/hw/ET_scraped_%s_%s.csv" % (user, year, month) # same as above
        #master_data = {0: {"Title": "Title", "Text": "Text"}}
        #txt = open(download_dir1, "w")
        #csv = open(download_dir2, "w")


        url = 'https://economictimes.indiatimes.com/archivelist/year-%s,month-%s,starttime-%s.cms' % (year, month, page_no)
        print(url)
        # get content of url
        page1 = requests.get(url)
        soup1 = BeautifulSoup(page1.content, 'html.parser')
        body1 = soup1.findAll(class_="pagetext")
        for articles in body1:
            links = articles.findAll("a")
            for link in links:
                link_url = link.get("href")
                print(link_url)
        page_no= page_no + 1
        #month = month + 1
    year = year + 1
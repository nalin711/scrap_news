import requests
from bs4 import BeautifulSoup
import newspaper

# Function to classify articles as EPU
def epu_classifier(content):
    str = content.lower()
    E = ["economic" , "economy"]
    U = ["uncertainty" , "uncertain"]
    P = ["regulation", "deficit", "legislation", "reform", "fiscal policy", "monetary policy", "central bank",
         "rbi", "reserve bank", "parliament", "finance ministry", "policy makers", "finance minister", "lawmakers",
         "niti ayog", "economic advisor", "prime minister's office", "pmo", "pmeac", "lok sabha", "tax", "taxes",
         "taxation", "excise duties", "custom duties", "gst"]
    for word in U:
        res_U = str.find(word)
        if res_U >= 0:
            break
    for word in P:
        res_P = str.find(word)
        if res_P >= 0:
            break
    for word in E:
        res_E = str.find(word)
        if res_E >= 0:
            break
    if (res_E >=0 and res_P >=0  and res_U >=0):
        return 1     # returns 1 ,i.e True if article is classifed as EPU
    else:
        return 0     # returns 0 ,i.e False if article is classifed as EPU

year = 2014

user = "nalinpriyaranjan"  # set user name here

while year <= 2018:
    month = 2           # set month counter
    while month <= 12:
        download_dir1 = "C:/Users/%s/PycharmProjects/hw/FE_scraped_%s_%s.txt" % (user, year, month) # remane this based on pycharm project directory
        download_dir2 = "C:/Users/%s/PycharmProjects/hw/FE_scraped_%s_%s.csv" % (user, year, month) # same as above
        master_data = {0: {"Title": "Title", "Text": "Text"}}
        txt = open(download_dir1, "w")
        csv = open(download_dir2, "w")

        page_no = 1
        last_page = 2
        while page_no <= last_page:
            url = 'https://www.financialexpress.com/archive/%s/%s/?page=%s' % (year, month, page_no)
            print(url)

            page1 = requests.get(url)
            soup1 = BeautifulSoup(page1.content, 'html.parser')
            body1 = soup1.findAll(class_="stories")
            i = 0
            for articles in body1:
                links = articles.findAll("a")
                for link in links:
                    link_url = link.get("href")
                    art = newspaper.Article(link_url)
                    art.download()
                    art.parse()
                    # print(art.title)
                    # print(art.text)
                    # master_data[i+1]={"Title":"%s"%art.title, "Text":"%s"%art.text}
                    txt.write("Title: %s" % art.title + "\n" + "Text:%s" % art.text)

                    csv.write("Title: %s" % art.title + "\t" + "\t EPU:\t %s\n " % epu_classifier(art.text))
                    # print(master_data[i+1])
                    i = i + 1

            page = requests.get(url)
            soup = BeautifulSoup(page.content, 'html.parser')
            body = soup.findAll(class_="next")
            # i = 0
            for articles in body:
                links = articles.findAll("a")
                for link in links:
                    link_url = link.get("href")
                    # print(link_url[:])
                    if page_no >= 9:
                        last_page = int(link_url[-2:])
                    else:
                        last_page = int(link_url[-1:])

            page_no = page_no + 1
        print ("Last page has arrived")
        month = month + 1
year = year + 1
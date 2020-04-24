from urllib.request import Request, urlopen as urReq
from bs4 import BeautifulSoup as soup

def scrapCertainUrl(url):
    #send headers to act as a browser
    r = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    #send request
    uClient = urReq(r)
    page_html = uClient.read()
    uClient.close ()
    return soup(page_html, "html5lib")

f = open("themeforest.csv" , "w")
f.write ("title, category, price, sales, publish_date, trending\n")
for i in range(1,5):
    page_soup = scrapCertainUrl('https://themeforest.net/category/wordpress?sort=date&page=' + str(i))
    themes = page_soup.findAll ("li" , {"class":"_1cn3x"})
    for theme in themes: 
        title= theme.find("a", {"class":"_2Pk9X"}).text
        category= theme.findAll("a", {"class":"R8zaM"})[1].text
        price= theme.find("div", {"class":"-DeRq"}).text
        sales= theme.find("div", {"class":"_3QV9M"})
        publish_date= theme.find("span", {"class":"_3TIJT"}).text
        if sales :
            sales= sales.text.strip("Sales")
        else:
            sales = 'NONE'
        
        trending= theme.find("img", {"class":"_1scd5"})
        if trending:
            trending = "YES"
        else:
            trending = "NO"

        f.write (title.replace(",", " ") + ", " + category + ", " +  price + ", " + sales + ", " + publish_date + ", " + trending + "\n")
        

f.close()
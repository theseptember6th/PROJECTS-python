from plyer import notification
import requests
from bs4 import BeautifulSoup

def notifyMe(title,message):
    notification.notify(
        title=title,
        message=message,
        app_icon=r'C:\Users\Kristal\Desktop\PROJECTS-python\PROJECT 5\corona.ico', #app icon supports .ico file and not .png files
        timeout=10   #notification will be shown for 10 seconds
    )

def getData(url):
    r=requests.get(url)
    return r.text


if __name__=="__main__":
    # notifyMe("kristal","lets stop the spread of the virus together")
    html_data=getData("https://prsindia.org/covid-19/cases")
    # print(html_data)
    soup = BeautifulSoup(html_data, 'html.parser')
    # print(soup.prettify())
    itemlist=[]
    for tr in soup.find_all('tbody')[0].find_all('tr'):
       #print(tr.get_text())
       itemlist.append(tr.get_text().split('\n'))
    
    print(itemlist)

    states=["Andhra Pradesh","Uttar Pradesh","Punjab"]

    for item in itemlist:
        if item[0] in states:
            print(item)

       
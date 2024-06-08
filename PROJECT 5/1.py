from plyer import notification
import requests
from bs4 import BeautifulSoup

def notifyMe(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon=r'C:\Users\Kristal\Desktop\PROJECTS-python\PROJECT 5\corona.ico',  # Ensure the path is correct
        timeout=10  # Notification will be shown for 10 seconds
    )

def getData(url):
    r = requests.get(url)
    return r.text

if __name__ == "__main__":
    # notifyMe("kristal", "Let's stop the spread of the virus together")
    html_data = getData("https://prsindia.org/covid-19/cases")
    soup = BeautifulSoup(html_data, 'html.parser')
    
    itemlist = []
    for tr in soup.find_all('tbody')[0].find_all('tr'):
        tds = [td.get_text(strip=True) for td in tr.find_all('td')]
        if len(tds) == 5:  # Ensure correct number of columns
            itemlist.append(tds)
    
    print(itemlist)

    states = ["Andhra Pradesh", "Uttar Pradesh", "Punjab"]

    for item in itemlist:
        if item[1] in states:  # Assuming state name is in the second column
            state, confirmed, active, cured, death = item[1], item[2], item[3], item[4], item[5]
            print(f"State: {state}, Confirmed: {confirmed}, Active: {active}, Cured: {cured}, Deaths: {death}")
            notifyMe(f"COVID-19 Update for {state}", f"Confirmed: {confirmed}, Active: {active}, Cured: {cured}, Deaths: {death}")

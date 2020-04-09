from plyer import notification
import requests
from bs4 import BeautifulSoup
import time

def notifyMe(title,message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "E:\cronavirus\download.ico",
        timeout =6
    )

def getData(url):
    r=requests.get(url)
    return r.text

if __name__ == "__main__":
    while True:
    #notifyMe("shishir","stop the spread of this virus together") 

        myHtmlData = getData('https://www.mohfw.gov.in/')
        #print(myHtmlData)
        soup = BeautifulSoup(myHtmlData, 'html.parser')
        #print(soup.prettify())
        myDataStr = ""

        for tr in soup.find_all('tbody')[0].find_all('tr'):
            myDataStr += tr.get_text()
        myDataStr = myDataStr[1:]
        
        itemList = myDataStr.split("\n\n")

        states = ['Bihar','Delhi','West Bengal','Uttar Pradesh']
        for item in itemList[0:31]:
            dataList = item.split('\n')
            if dataList[1] in states:
                #print(dataList)
                nTitle = 'cases of covid_19'
                ntext = f"State {dataList[1]}\nTotal Confirmed cases: {dataList[2]}\nCured/Discharged/:{dataList[3]}\nDeath:{dataList[4]}"
                notifyMe(nTitle,ntext)
                time.sleep(3)
        time.sleep(20)
    
 
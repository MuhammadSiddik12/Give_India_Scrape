import requests
import json 
from bs4 import BeautifulSoup 
page = requests.get("https://www.giveindia.org/certified-indian-ngos")
soup = BeautifulSoup(page.text , "html.parser")

def scrape_give_india() :
    d,li={},[]
    main_div = soup.find('table' , class_="jsx-697282504 certified-ngo-table")
    all_tr = main_div.find_all('tr',class_="jsx-697282504")
    for div,cause in zip(range(1,len(all_tr)),range(1,len(main_div)+1)):
        d['Name'] = all_tr[div].find('div',class_="col").text
        d['State']=all_tr[cause].find_all('td',class_='jsx-697282504')[-1].text
        d['Cause']=all_tr[cause].findAll('td',class_='jsx-697282504')[-2].text
        li.append(d.copy())

    with open ('WSGivenIndia.json', 'w') as wr:
        wr.write(json.dumps(li,indent=4))
        wr.close()
    
    a=input("Enter a name of NGOs, State or Cause:\n")
    for i in li:
        if a in  i.values():
            print(i)
scrape_give_india()

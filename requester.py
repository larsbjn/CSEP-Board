import requests
from bs4 import BeautifulSoup

def get_cantine_weekly_menu():  
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    url = 'http://torvekoekken.info/kantiner/incuba'
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    div = soup.find('div', {'class': 'entry-content'})
    children = div.findChildren("p" , recursive=True)
    menu = []
    menu.append([children[3].text, children[4].text])
    menu.append([children[6].text, children[7].text])
    menu.append([children[9].text, children[10].text])
    menu.append([children[12].text, children[13].text])
    menu.append([children[15].text, children[16].text])
    menu.append(["Bajer", "Bajer"])
    menu.append(["Treo", "Treo"])
    return(menu)


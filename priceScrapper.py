import requests
from bs4 import BeautifulSoup
import yagmail

yag = yagmail.SMTP('hendryratnam07@gmail.com',oauth2_file='~/oauth2_creds.json')
url = 'https://www.newegg.com/p/pl?d=gpu'

r = requests.get(url).text
soup = BeautifulSoup(r,'html.parser')

# New egg parsing
items = soup.find_all('div','item-container')
itemAction = soup.find_all('div','item-action')
neweggItemNames = []
neweggItemPrices = []

for item in items:
    #print(item.find('img')['title'])
    neweggItemNames.append(str(item.find('img')['title']))

for item in itemAction:
    neweggItemPrices.append(str(item.ul.find('li','price-current').strong))

wow = ""

contents = '''


'''
#yag.send(to='hendryratnam@gmail.com', contents=neweggItemNames.pop())
while len(neweggItemNames) is not 0:
    wow = neweggItemNames.pop()
    print(wow)
    print('')


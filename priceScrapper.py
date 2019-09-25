import requests
from bs4 import BeautifulSoup
from emailer import sendEmail

def neweggParser(search):
    url = 'https://www.newegg.com/p/pl?d='+search

    # Send the request to the url and convert to text
    # Make the soup bs4 soup object
    r = requests.get(url).text
    soup = BeautifulSoup(r,'html.parser')

    # Find all the items located in item-container css class
    items = soup.find_all('div','item-container')
    itemAction = soup.find_all('div','item-action')
    itemLinks = soup.find_all('a','item-img')

    # Some vars to hold prcies and names
    # Add links later
    neweggItemNames = []
    neweggItemPrices = []
    neweggLinks = []

    # Go through all items and find the title
    for item in items:
        #print(item.find('img')['title'])
        neweggItemNames.append(str(item.find('img')['title']))

    # Go through all class itemAction to find prices
    for item in itemAction:
        neweggItemPrices.append(item.ul.find('li','price-current').strong.text.strip())

    for link in itemLinks:
        neweggLinks.append(link['href'])

    # Debug stuff
    wow = ""

    # while len(neweggItemNames) and len(neweggItemPrices) is not 0:
    #     wow = neweggItemNames.pop()
    #     print(wow)
    #     wow = neweggItemPrices.pop()
    #     print(wow)
    #     print('')
    return contentFormatter(neweggItemNames,neweggItemPrices,neweggLinks)

def contentFormatter(name,price,links=None):
    content = []
    if links is None:
        while len(name) and len(price) is not 0:
            content.append(str('<p>' + name.pop() + ' For ' + price.pop()) + '</p>')
    else:
        while len(name) and len(price) is not 0:
            content.append(str('<p><a href='+links.pop()+'>' + name.pop() + ' For ' + price.pop() + '</a></p>'))

    return content
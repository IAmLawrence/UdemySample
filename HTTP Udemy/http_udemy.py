import requests
import bs4

hold_website = requests.get('https://www.odoo.com')
var_soup = bs4.BeautifulSoup(hold_website.text)
hold_element = var_soup.select('div')
print("THIS> ", hold_element[2].getText())
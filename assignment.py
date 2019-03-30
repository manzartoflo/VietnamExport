from selenium import webdriver
from bs4 import BeautifulSoup

url = "http://en.vietnamexport.com/index.php/component/k2/itemlist/category/63-machine-and-equipment.html"
req = webdriver.Firefox()
req.get(url)
html = req.execute_script('return document.documentElement.outerHTML')
soup = BeautifulSoup(html, 'lxml')
print(soup.prettify())
div = soup.findAll('div', {'class': 'tintuc_item'})
text = '/html/body/div[2]/div[1]/div/div[1]/div[3]/div[4]/ul/li[13]/strong'
file = open('assignment.csv', 'w')
header = 'Company name, Email, Telephone\n'
file.write(header)

for i in range(9):
    for element in div:
        name = element.h3.text
        name = name.split('\t\t')[1].split('\t')[0]
        
        email = element.a.text
        if(len(email) == 0):
            email = 'NaN'
        
        telephone = str(element.div)
        telephone = telephone.split('Telephone')[1].split('<br/>')[0].split(':')[1]
        if(len(telephone) < 8):
            telephone = 'NaN'
        
        
        print(name + "\t" + email + "\t" + telephone)
        file.write(name.replace(',', '') + ',' + email.replace(',', '|') + ',' + telephone.replace(',', '|') + '\n')
    
    if(i != 8):
        find = find = req.find_element_by_xpath(text)
        find.click()
        html = req.execute_script('return document.documentElement.outerHTML')
        soup = BeautifulSoup(html, 'lxml')
        div = soup.findAll('div', {'class': 'tintuc_item'})
        
file.close()

import pandas as pd
f = pd.read_csv('assignment.csv')


#Telephone
#ap = str(div[0].div)
#ap.split('Telephone')[1].split('<br/>')[0].split(':')[1]

#email
#ap = div[0].a.text

#name
#ap = div[2].h3.text
#ap.split('\t\t')[1].split('\t')[0]
#text = '/html/body/div[2]/div[1]/div/div[1]/div[3]/div[4]/ul/li[13]/strong'
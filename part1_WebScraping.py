import requests
from bs4 import BeautifulSoup
import mysql.connector

print('Zakhire kardan Brand-Name-Price az site DIGISTYLE dakhel database')
print()
print('INFORMATION YOUR DATABASE')
u = input('Please enter your user of database : ')
p = input('Please enter your pass of database : ')
h = input('Please enter your host of database : ')
cnx = mysql.connector.connect(user=u, password=p, host=h, database='DigiStyle')
# print ('connected to db :)')
cursor = cnx.cursor()

newBrand = list()
newName = list()
newPrice = list()
for i in range(1, 63): #WARNING FOR 2 OR 63
    r = requests.get('https://www.digistyle.com/category-men-tee-shirts-and-polos/?pageno=%s&sortby=4' %i)
    soup = BeautifulSoup(r.text, 'html.parser')
    brand = soup.find_all('span', attrs={'class': 'c-product-item__brand'})
    name = soup.find_all('span', attrs={'class': 'c-product-item__name'})
    price = soup.find_all('span', attrs={'class': 'c-product-item__price-value'})

    for i in range(0, 36):
        b = brand[i]
        b = str(b)
        b = b[36:-7]
        n = name[i]
        n = str(n)
        n = n[35:-7]
        p = price[i]
        p = str(p)
        p = p[42:-7]
        sql = 'INSERT INTO Digistyle (brand_of_product, name_of_product, price_of_product) VALUES (%s, %s, %s)'
        val = (b, n, p)
        cursor.execute(sql, val)

cnx.commit()
cnx.close()

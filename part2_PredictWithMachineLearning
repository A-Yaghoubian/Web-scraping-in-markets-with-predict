import mysql.connector
from sklearn import tree
from sklearn import preprocessing

print('Khandan etelaat az database va estefade az ML roye an')
print()
print('INFORMATION YOUR DATABASE')
u = input('Please enter your user of database : ')
p = input('Please enter your pass of database : ')
h = input('Please enter your host of database : ')
cnx = mysql.connector.connect(user=u, password=p, host=h, database='DigiStyle')
# print ('connected to db :)')
cursor = cnx.cursor()

query = 'SELECT * FROM DigiStyle;'
cursor.execute(query)

brand = list()
name = list()
price = list()

for (brand_of_product, name_of_product, price_of_product) in cursor:
    brand.append(brand_of_product)
    name.append(name_of_product)
    price.append(price_of_product)

x = []
y = []
z = []

lex = preprocessing.LabelEncoder()
lex = lex.fit_transform(brand)

ley = preprocessing.LabelEncoder()
ley = ley.fit_transform(name)

for i in range(0, 36*62):
    z.append([lex[i], ley[i]])
    y.append(price[i])

clf = tree.DecisionTreeClassifier()
clf = clf.fit(z, y)

print('FOR PREDICT : ')
your_brand = input('Enter Brand : ')
your_name = input('Enter name : ')

lx = preprocessing.LabelEncoder()
lx = lx.fit_transform(brand)

ly = preprocessing.LabelEncoder()
ly = ly.fit_transform(name)

new_data = [lx, ly]
answer = clf.predict(new_data)
print('Predict Of Price : %s' %answer)

cnx.close()

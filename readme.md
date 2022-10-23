# Create and get from ORM
* To insert data:
```
 session.add(ORMModel(**SchemaModel.dict()))
 session.commit()
```
* to get data:
  * one
```
session.query(City).filter(City.id == city.id).first()
```
  * all
```
session.query(City).all()
```

 * now create model city (See this file:  `scripts/files/cities.csv` to know properties )
 * create migration and run
 * create schema
 * create folder name database_sql/queries (This folder will contains all queries needed to our api)
 * inside this folder create a file named city.py 
 * create a class named `CityQueries` 
 * then add method add and all
 * method add will add data to our database
 * mothod all will return all data in this table
 * create `CityServices` with methods add and all, that will call the same methods in `CityQueries` 
 * add route post and get `/` to insert and show data
 * congrats 
 * now a real case upload 10000 files from csv
 * to read csv
```
import csv
with open('eggs.csv', newline='') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=',')
     for row in spamreader:
        print(', '.join(row))
```
* to make a post in python
```
import requests

url = 'https://www.w3schools.com/python/demopage.php'
myobj = {'somekey': 'somevalue'}

x = requests.post(url, json = myobj)

print(x.text)
```
* now read cities.csv and post this data in our api
* rember our base url: "http://127.0.0.1:8000/city"
* our post payload:
```
{
    "id":2,
    "name":"city test",
    "country":"country test"
}
```
* hint DictReader allows convert row in dict: 
```
spamreader = csv.DictReader(csvfile, delimiter=',',fieldnames=['country','id','name'])

```
* the result of DictReader you can covert to list 
```
#this sub list avoid first element in csv (hearders)
 list(spamreader)[1:] 
```
* now delete all elements!
* using the logic before add remove all elements
```
 session.query(City).filter(City.id == id).delete()
        session.commit()
```
* create a script to remove all elements
```
response = requests.get(URL)
    json_data = response.json()
```
* for delete
```
response = requests.delete(f'{URL}/{id}')
```

* congrats
  * next steps: relations, batch, dependencies, async
  
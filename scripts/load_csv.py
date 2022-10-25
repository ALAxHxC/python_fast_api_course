import csv
import requests

URL = 'http://127.0.0.1:8000/city'
def create_city(row):
    response = requests.post(URL, json={
        "id": int(row['id']),
        "name":  row['name'],
        "country": row['country']
    })
    return response.status_code


with open('files/cities.csv', newline='') as csvfile:
    spamreader = csv.DictReader(csvfile, delimiter=',',fieldnames=['description','country','id','name'])
    result = map(lambda row:create_city(row) ,list(spamreader)[1:])
    print(list(result))


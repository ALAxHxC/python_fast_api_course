import csv
import requests

def createCities(row):
    responde = requests.post("http://127.0.0.1:8000/cities", json={
        "country": row["country"],
        "cod_name": row["cod_name"],
        "name": row["name"]})
    return responde.status_code

with open("cities.csv", newline="") as csvfile:
    spamreader = csv.DictReader (csvfile, delimiter=",", fieldnames=["description", "country", "cod_name", "name"])
    result= map (lambda row: createCities(row), list (spamreader))
    print(list(result))


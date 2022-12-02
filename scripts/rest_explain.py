
import requests

if __name__ == "__main__":
    cities = requests.get("http://127.0.0.1:8000/cities")
    city = filter(lambda item: item.get('cod_name')==88, cities.json())
    print(list(city))
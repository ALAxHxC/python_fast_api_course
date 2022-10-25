import requests

URL = 'http://127.0.0.1:8000/city'
def delete_city(id):
    print(f'{URL}/${id}')
    response = requests.delete(f'{URL}/{id}')
    return response.status_code, id
def list_cities():
    response = requests.get(URL)
    json_data = response.json()
    data = map(lambda city: delete_city(city['id']), json_data)
    print(list(data))
list_cities()
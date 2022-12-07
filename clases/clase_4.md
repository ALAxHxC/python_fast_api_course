# Validacion de datos:

* Debemos validar que al registrar un vehiculo exista:
  * la marca
  * la linea
  * la ciudad
* Agregar Tabla Usuario vehiculo:
````

class UserVehicule(Base):
    __tablename__ = "vehicle"

   #id_vehiculo
   #id_usuario
   #placa_del_vehiculo
   #fecha_de_registro
````

* Agregar la propiedad unica de correo a usuario
* Borrar usuarios y volver a crear 1.
* Registrar 1 usuario
* Asociar un vehiculo a ese usuario
* Cuando se registr un vehiculo enviar un correo electronico
* base:
````
curl --request POST \
  --url https://api.sendinblue.com/v3/smtp/email \
  --header 'accept: application/json' \
  --header 'api-key:YOUR_API_KEY' \
  --header 'content-type: application/json' \
  --data '{  
   "sender":{  
      "name":"Sender Alex",
      "email":"senderalex@example.com"
   },
   "to":[  
      {  
         "email":"testmail@example.com",
         "name":"John Doe"
      }
   ],
   "subject":"Hello world",
   "htmlContent":"<html><head></head><body><p>Hello,</p>This is my first transactional email sent from Sendinblue.</p></body></html>"
}'
````
* Recordemos el tutorial de youtube
````
import requests

if __name__ == "__main__":
    cities = requests.get("http://127.0.0.1:8000/cities")
    city = filter(lambda item: item.get('cod_name')==88, cities.json())
    print(list(city))
````
* Al crear el usuario se envio el correo?
* Validar que no hayan emails duplicados
* Felicitaciones por tu progreso
* Tareas:
    * Calificacion: X
    * Recomendaciones: X
    * Cosas buenas: x
    * Cosas por mejorar: x
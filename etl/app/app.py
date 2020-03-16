import requests
from os import environ
from pymongo import MongoClient

response = requests.get('https://raw.githubusercontent.com/hector-vido/flask-api/master/samples/usuarios.csv')
usuarios = response.text.split('\n')[1:]

client = MongoClient('mongodb://{0}:{1}@{2}:27017/admin'.format(environ['MONGO_USER'], environ['MONGO_PASS'], environ['MONGO_HOST']))
db = client.acme

for u in usuarios:
    u = u.split(',')
    if len(u) != 5:
        break
    elif float(u[4]) < 3000:
        continue
    db.usuarios.insert_one({'_id' : int(u[0]), 'name' : u[1], 'email' : u[2], 'gender' : u[3], 'salary' : float(u[4])})

from urllib import request
from json import loads

with request.urlopen("https://geolocation-db.com/json") as url:
    data = loads(url.read().decode())

print(list(data.values()))


# Las siguientes funciones han sido planteadas para la recolección de datos de la API Spotify.
# Las utilizaremos para iterar a través de los datos recolectados en el scrapeo de El Ártico Discos
# Con ellas se pretende enriquecer la información ya obtenida.
import requests as req
import time

def get_rank(album_name):
    time.sleep(0.3)
    url = f'https://api.deezer.com/search?q=album:"{album_name}"'
    dictio = {} 

    res = req.get(url)
    if res.status_code == 200:
        try:
            for i in res.json()['data']:
                track = i['title']
                rank = i['rank']
    
                dictio[track] = rank
        except:
            return None
    else:
        return None
    return dictio
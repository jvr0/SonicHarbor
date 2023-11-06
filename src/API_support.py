# La siguiente función es utilizada para la recolección de datos de la API Deezer. 
# Entra el nombre de un album (el cual se ha recogido durante el scrapeo) y sale un diccionario.
# El diccionario contiene el nombre de las canciones del album como keys y la puntuación cómo valor.
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
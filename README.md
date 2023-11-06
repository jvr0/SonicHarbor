# SonicHarbor

La compañía [El Ártico Discos](https://www.discogs.com/es/seller/elarticodiscos/profile "El Ártico Discos"). nos ha encargado el siguiente proyecto. Desean una recolección de los últimos 10.000 artículos presentados a la venta en la plataforma Discogs. El motivo de este encargo han sido una serie de artículos, los cuales, presentan el incremento de las ventas de aquellos albumes musicales que se presentan en 'The 500 Greatest Albums of All Time' de la revista Rolling Stone. Quieren que revisemos su inventario y comprobemos cuantos de estos mejores 500 albumes tienen a la venta.

![portada](https://github.com/jvr0/SonicHarbor/blob/main/img/SonicHarbor.png)

#### Table of contents
1. [Recopilación](#recopilacion)
    1. [500 Greates Albums](#greatest)
    2. [El Ártico Discos](#artico)
    3. [Deezer Api](#api)
2. [Análisis](#analisis)

# 1. Recopilación <a name="recopilacion"></a>

## I. 500 Greatest Albums <a name="recopilacion"></a>

Para realizar la comparación encargada por la compañía fue necesario acceder a los 500 mejores albumes presentados por la revista Rolling Stone. Esta información fue recuperada de la base de datos: [Rolling Stone's 500 Greatest Albums of All Time](https://www.kaggle.com/datasets/notgibs/500-greatest-albums-of-all-time-rolling-stone "Rolling Stone's 500 Greatest Albums of All Time") en la plataforma Kaggle. Este dataset vino dado en un csv, presenta datos sobre el artista, el album y el año la release, entre otros. Se presenta la información dada por la revista en 2012, donde revisaron la lista original. 

## II. El Ártico Discos <a name="artico"></a>

Nuestro siguiente paso fue la recopilación del artista, album, sello musical, estado del disco, estado de la funda, precio, gastos de envio y precio final de los últimos 10.000 items registrados en la tienda online. Para la recopilación de estos datos se ha utilizado el notebook '1_scraping'. El procedimiento ha consistido en recopilar los datos de 250 en 250 y por cada iteración enviar los resultados a la recien creada base de datos sonic_harbor en MongoDB.

<details>
<summary>Diagráma</summary>
<br>

Diagráma del proceso de recogida de datos 
![diagrama](https://github.com/jvr0/SonicHarbor/blob/main/img/Extracción.png)

</details>

<details>
<summary>Función Items</summary>
<br>

```python
def item(driver):
    
    items = driver.find_elements(By.CLASS_NAME, 'item_description')

    item_description = []

    try:

        for i in items:

            temp = []

            name = i.find_element(By.CLASS_NAME, 'item_description_title').text.split('-')[0][:-1]
            temp.append(name)

            album = i.find_element(By.CLASS_NAME, 'item_description_title').text.split('-')[1].split('(')[0]
            temp.append(album[1:-1])

            label = i.find_element(By.CLASS_NAME, 'hide_mobile.label_and_cat').text.split('\n')[0].split(':')[1]
            temp.append(label)

            item_condition = i.find_element(By.CSS_SELECTOR, 'td.item_description > p.item_condition > span:nth-child(3)').text
            temp.append(item_condition)

            sleeve_condition = i.find_element(By.CLASS_NAME, 'item_sleeve_condition').text
            temp.append(sleeve_condition)

            item_description.append(temp)

    except:
        print('no se pudo, amigo...')
        
    return item_description
```
    
</details>

<details>
<summary>Función Price</summary>
<br>

```python
def price(driver):

    prices = driver.find_elements(By.CLASS_NAME, 'item_price.hide_mobile')

    price_description = []

    for i in prices:

        temp = []

        try:
            price = i.find_element(By.CLASS_NAME, 'price').text.split('€')[1].replace(',','.')
            temp.append(float(price))
        except:
            temp.append(0)

        try:
            ship = i.find_element(By.CLASS_NAME, 'hide_mobile.item_shipping').text.split(' ')[0].split('€')[1].replace(',','.')
            temp.append(float(ship))
        except:
            temp.append(0)

        try:
            final = i.find_element(By.CLASS_NAME, 'converted_price').text.split(' ')[0][1:].replace(',','.')
            temp.append(float(final))
        except:
            temp.append(0)

        price_description.append(temp)

    return price_description
```

</details>

<details>
<summary>Función Next</summary>
<br>

```python
def next_page(driver):

    driver.execute_script("window.scrollBy(0, 500);")

    wait = WebDriverWait(driver, 10)  # Espera hasta 10 segundos como máximo
    next_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'pagination_next')))
    next_button.click()
```
    
</details>

    
## III. Deezer API <a name="api"></a>

Una vez se recogieron los datos de la revista Rolling Stone y del inventario de El Ártico Discos se decidió enriquecer estos últimos añadiendo el nombre y puntuación de las canciones dentro de cada album registrado. Para ello se ha utilizado la API musical Deezer. Aplicando una función previamente construida al data frame exportado de nuestra nueva base de datos en MongoDB se recogieron estos nuevos datos para posteriormente añadirlos al registro del inventario. Tras el enriquecimiento se realiza la actualización de la base de datos.


# 2. Análisis y conclusiones <a name="analisis"></a>

Finalmente, con los datos preparados, procedemos a la comparación requerida por el cliente. Observamos que de los últimos 10.000 items publicados 25 de ellos pertenecen a la lista de los mejores 500 albumes de la revista Rolling Stone. 

Cómo curiosidad vemos que el precio medio de estos items es de 15.43 euros. También queda registrado que la mayoría de albumes son de Rock, 18 de ellos. El 64% de los items y el 92% de las fundas se encuentran en una condición excelente (Near Mint (NM or M-)). Además, éxiste un producto Mint (M), del cual se podría revisar el precio.

A continuación dejamos el desglose del análisis de los precios.

<details>
<summary>Desglose</summary>
<br>

![desglose](https://github.com/jvr0/SonicHarbor/blob/main/img/price.png)

</details>

##### Mongo Query
A mayores del análisis realizado en el cuarto notebook se ha creado un quinto archivo con algunas queries que nuestro cliente podría utilizar en la nueva base de datos de MongoDB. A continuación se presentan:

<details>
<summary>10 items más caros del inventario con precio final superior a 50</summary>
<br>
```
query = {'final_price': {'$gte':70}}

select = {'_id':False, 'album': 1, 'final_price':1}

list(inven.find(query,select).limit(10).sort('final_price', -1))
```
</details>

<details>
<summary>Albums a la venta de los beattles ordenados por precio</summary>
<br>
```
query = {'author': 'The Beatles'}

select = {'_id':False, 'author': 1, 'album':1}

list(inven.find(query,select).sort('final_price', -1))
```
</details>

<details>
<summary>Aquellos articulos sin gasto de envió e item condition near mint, busqueda limitada a los 5 más caros</summary>
<br>
```
query = {'ship_price': 0,
         'item_condition': 'Near Mint (NM or M-)'}

select = {'_id':False, 'album': 1, 'ship_price':1, 'final_price':1}

list(inven.find(query,select).limit(5).sort('final_price', -1))
```
</details>

<details>
<summary>Los discos con sleeve_condition Very Good (VG) y precio final entre 10 y 20</summary>
<br>
```
query = {'$and': [{'final_price': {'$gte':10}},
                 {'final_price': {'$lte':20}},
                 {'sleeve_condition': 'Very Good (VG)'}]}

select = {'_id':False, 'album': 1, 'final_price':1, 'sleeve_condition':1}

list(inven.find(query,select).limit(5).sort('final_price', -1))
```
</details>
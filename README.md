# SonicHarbor

La compañía [El Ártico Discos](https://www.discogs.com/es/seller/elarticodiscos/profile "El Ártico Discos"). nos ha encargado el siguiente proyecto. Desean una recolección de los últimos 10.000 artículos presentados a la venta en la plataforma Discogs. El motivo de este encargo han sido una serie de artículos, los cuales, presentan el incremento de las ventas de aquellos albumes musicales que se presentan en 'The 500 Greatest Albums of All Time' de la revista Rolling Stone. Quieren que revisemos su inventario y comprobemos cuantos de estos mejores 500 albumes tienen a la venta.

![portada](https://github.com/jvr0/SonicHarbor/blob/main/img/SonicHarbor.png)

#### Table of contents
1. [Recopilación](#recopilacion)
    1. [500 Greates Albums](#greatest)
    2. [El Ártico Discos](#artico)
    3. [Spotify Api](#api)
2. [Limpieza](#limpieza)
3. [Análisis](#analisis)

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

## III. Spotify API <a name="api"></a>


# 2. Transformación <a name="limpieza"></a>
The first paragraph text

# 3. Análisis y conclusiones <a name="analisis"></a>



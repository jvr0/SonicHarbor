from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


# La siguiente función nos sirve para obtener el precio durante el scrapeo.
# Entra el driver y sale una lista de listas, donde los elementos son: price, ship_price y final_price
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

# La siguiente función nos sirve para obtener las características del item durante el scrapeo.
# Entra el driver y sale una lista de listas, donde los elementos son las caracteristicas scrapeadas:
# (name, album, label, item_condition, sleeve_condition)
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

# La siguiente función nos sirve para pasar a la siguiente página del scrapeo.
# Entra un driver y utiliza selenium para scrollear un poco hacia el boton, a continuación espera hasta
# que el boton de siguiente esta disponible y finalmente hace click para pasar de página.
def next_page(driver):

    driver.execute_script("window.scrollBy(0, 500);")

    wait = WebDriverWait(driver, 10)  # Espera hasta 10 segundos como máximo
    next_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'pagination_next')))
    next_button.click()
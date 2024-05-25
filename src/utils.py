from types_src import *
import time

# pop up para cuando la pagina se cargo correctamente
loading_success = '//*[@id="frmLstOfertsLabo:mensaje_container"]/div/div/div[2]/p'

def query_success(driver: WebDriver):
    """
    Verifica que si despues de aplicar los filtros se 
    carga los elementos correctos y da 1 segundo adicional
    para poder cargar
    """
    def success():
        find = driver.find_elements(By.XPATH, loading_success)
        return find, len(find) > 0 #encontro el elemento
    find, popup = success()
    while not popup:
        print('loading', popup)
        find, popup = success()
    print(find[0].text)
    time.sleep(1) 
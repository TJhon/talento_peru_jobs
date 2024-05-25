
# aplicacion de los filtros

from types_src import *
import time

# location dropdown (ubicacion)

region_filter_dropdown = '//*[@id="frmLstOfertsLabo:cboDep"]/div[3]/span'
ID_index = "frmLstOfertsLabo:cboDep_{}"
apply_filter = '//*[@id="frmLstOfertsLabo:j_idt42"]/span'
# #


# //*[@id="frmLstOfertsLabo:cboDep_1"]
def filter_region(driver: WebDriver, n_list: int):
    """
    Seleccciona por el id la ubicacion y aplica el filtro
    """

    # seleccionar filtro
    driver.find_element(By.XPATH, region_filter_dropdown).click()
    time.sleep(1)
    item_drop = driver.find_element(By.ID, ID_index.format(n_list))
    # print(ID_index.format(n_list))
    location_main = item_drop.text
    print(location_main)
    item_drop.click()

    # aplicar filtro
    driver.find_element(By.XPATH, apply_filter).click()
    return location_main

    


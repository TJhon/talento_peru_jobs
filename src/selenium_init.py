from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time, pandas as pd
import json
from selenium.webdriver.common.action_chains import ActionChains


from data_in_page import get_info_page, get_info_box, get_n_positions


from filters_page import filter_region
from utils import query_success
from navigation_pages import navigate_to, page_num


driver = webdriver.Chrome()
driver.get(
    "https://app.servir.gob.pe/DifusionOfertasExterno/faces/consultas/ofertas_laborales.xhtml"
)

time.sleep(3)
print("complete loading")

location = filter_region(driver, 5)
query_success(driver)

total_positions_in_page = get_n_positions(driver)
begin_page, total_pages = page_num(driver)

data = get_info_page(driver, total_positions_in_page)

while begin_page < total_pages:
    begin_page, total_pages = navigate_to(driver)
    total_positions_in_page = get_n_positions(driver)
    result_page = get_info_page(driver, total_positions_in_page)
    data = pd.concat([data, result_page])
    # total1.append(total2)
    print(begin_page, total_pages)
import pandas as pd

data = pd.DataFrame(data)
data.to_csv(f"./data/{location}.csv", index=False)

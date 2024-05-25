from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time, re
from selenium.webdriver.common.action_chains import ActionChains

from data_in_page import get_info_page, get_info_box, get_n_positions

driver = webdriver.Chrome()
driver.get("https://app.servir.gob.pe/DifusionOfertasExterno/faces/consultas/ofertas_laborales.xhtml")

time.sleep(3)
print("complete loading")


from filters_page import filter_region
from utils import query_success
from navigation_pages import navigate_to, page_num

location = filter_region(driver, 2)
query_success(driver)
total_positions_in_page = get_n_positions(driver)
print(page_num(driver))
total1 = get_info_page(driver, total_positions_in_page)

# print(total1)
acutal_page = navigate_to(driver)

total_positions_in_page = get_n_positions(driver)
total2 = get_info_page(driver, total_positions_in_page)
print(acutal_page)

time.sleep(30)

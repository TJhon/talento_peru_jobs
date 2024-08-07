from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time, pandas as pd

from selenium.webdriver.common.action_chains import ActionChains
import pytz
import datetime

gmt5 = pytz.timezone("Etc/GMT+5")
today = datetime.datetime.now(gmt5).strftime("%d-%m-%Y")


from .data_in_page import get_info_page, get_info_box, get_n_positions
from .filters_page import filter_region
from .utils import query_success
from .navigation_pages import navigate_to, page_num


def scrapper(options=None, n_reg=1, github=False):

    if options is not None:
        driver = webdriver.Chrome(options=options)
    else:
        driver = webdriver.Chrome()
    driver.get(
        "https://app.servir.gob.pe/DifusionOfertasExterno/faces/consultas/ofertas_laborales.xhtml"
    )
    time.sleep(20)
    if github:
        print("save screenshow")
        driver.save_screenshot("./logs/github.png")
        driver.quit()
        return "Save screenshot"

    print("complete loading")

    location = filter_region(driver, n_reg)
    query_success(driver)

    total_positions_in_page = get_n_positions(driver)
    begin_page, total_pages = page_num(driver)

    data = get_info_page(driver, total_positions_in_page)

    while begin_page < total_pages:
        begin_page, total_pages = navigate_to(driver)
        total_positions_in_page = get_n_positions(driver)
        result_page = get_info_page(driver, total_positions_in_page)
        data = pd.concat([data, result_page])
        print(begin_page, total_pages)

    driver.quit()
    # driver.save_screenshot("./img.png")
    data = pd.DataFrame(data)
    data.to_csv(f"./data/{today}_{location}.csv", index=False)

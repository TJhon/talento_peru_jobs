from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC


def complete_web(driver: WebDriver, xpath, time=30):
    try:
        element = Wait(driver, time).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
    finally:
        print("Failed to Load")
        driver.quit()

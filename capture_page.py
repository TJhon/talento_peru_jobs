import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Configurar opciones de Chrome
chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")  # Opcional: Para entornos con poca memoria compartida
chrome_options.add_argument("--headless")

# Inicializar Selenium con Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Navegar a la página
driver.get("https://www.google.com")

# Esperar 10 segundos para que la página cargue completamente
print("waiting")
time.sleep(10)

# Tomar captura de pantalla
driver.save_screenshot("captura_pagina.png")

# Cerrar el navegador
driver.quit()




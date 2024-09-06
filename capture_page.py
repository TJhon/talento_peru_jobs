import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager

# Configurar opciones de Firefox
firefox_options = Options()
firefox_options.add_argument("--headless")
firefox_options.add_argument("--disable-dev-shm-usage")  # Opcional: Para entornos con poca memoria compartida
firefox_options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0"
)

# Inicializar Selenium con Firefox
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=firefox_options)

# Navegar a la página
driver.get("https://app.servir.gob.pe/DifusionOfertasExterno/faces/consultas/ofertas_laborales.xhtml")

# Esperar 10 segundos para que la página cargue completamente
print("waiting")
time.sleep(10)

# Tomar captura de pantalla
driver.save_screenshot("captura_pagina.png")

# Cerrar el navegador
driver.quit()

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Configuración de Selenium para usar el driver de Chrome automáticamente
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Navegar a la página
driver.get("https://app.servir.gob.pe/DifusionOfertasExterno/faces/consultas/ofertas_laborales.xhtml")

# Esperar 10 segundos para asegurar que la página cargue completamente
time.sleep(10)

# Tomar la captura de pantalla
driver.save_screenshot("captura_pagina.png")

# Cerrar el navegador
driver.quit()

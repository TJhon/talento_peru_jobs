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
chrome_options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
)
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
# Inicializar Selenium con Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Navegar a la página
driver.get("https://app.servir.gob.pe/DifusionOfertasExterno/faces/consultas/ofertas_laborales.xhtml")

# Esperar 10 segundos para que la página cargue completamente
print("waiting")
time.sleep(10)

# Tomar captura de pantalla
driver.save_screenshot("captura_pagina.png")

# Cerrar el navegador
driver.quit()




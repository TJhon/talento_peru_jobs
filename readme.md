# Scrapeo de Oportunidades Laborales de SERVIR

Este proyecto realiza el scraping de ofertas laborales del portal oficial de [APPSERVIR](https://app.servir.gob.pe/DifusionOfertasExterno/faces/consultas/ofertas_laborales.xhtml), extrayendo datos relevantes sobre las oportunidades laborales publicadas por instituciones estatales en Perú. Dado que la página web está optimizada de manera subóptima, las peticiones de datos consumen una gran cantidad de recursos y tiempo, por lo que este proyecto busca optimizar el proceso mediante el uso de scraping eficiente y la implementación de una API para el acceso a los datos obtenidos.

### Problema Detectado
- **Carga ineficiente**: Por cada página, el sitio descarga ~1.8MB, y el tiempo de carga promedio es de 1.6 segundos.
- **Peticiones adicionales**: Cada vez que se consulta la descripción de un trabajo y se regresa a la página anterior, se descargan 6MB adicionales de archivos estáticos, lo que genera tiempos de espera de 2-4 segundos por cada interacción.
- **Comparación con APIs modernas**: Hacer una petición a una API basada en Vercel que devuelve datos de ~3.5k empleos (filas) solo consume 1.2MB, mostrando una mejora considerable en eficiencia.

> [!WARNING]
> Este proyecto está actualmente en desarrollo. Los datos recolectados hasta ahora se encuentran disponibles en la siguiente carpeta del repositorio, organizados en archivos CSV con el formato `dd-mm-yyyy.csv`.
> Carpeta de datos recolectados: [Data CSVs](https://github.com/TJhon/talento_peru_jobs/tree/description_jobs_ubication/data/all)

> [!IMPORTANT]  
> La página de SERVIR bloquea peticiones desde IPs que no estén ubicadas en Perú, asi que todavia no se puede automatizar con GitHub Actions, ni con otras shells. Tampoco fue eficaz usar proxies gratis

## Estructura del Proyecto

- **Scraping**: Recolecta datos de la página de SERVIR, incluyendo detalles como título de trabajo, institución, salario, fecha de publicación, y más.
- **API (FastAPI)**: Una API que expone los datos scrapeados para consultas más rápidas y eficientes.
- **Automatización**: Plan futuro para automatizar el scraping y despliegue del proyecto con GitHub Actions y Vercel.

## Requisitos

Para ejecutar este proyecto, necesitarás instalar los paquetes requeridos, los cuales se encuentran en el archivo `requirements.txt`.

```bash
pip install -r requirements.txt
```

## Uso del Scraping

Para ejecutar el script que realiza el scraping y extrae los datos:

```bash
python main_details.py
```

Este script recolectará información sobre las oportunidades laborales y guardará los datos en una base de datos o en un archivo CSV, dependiendo de la configuración.

## Uso de la API

El proyecto también incluye una API basada en FastAPI que permite consultar los datos recolectados.

### Iniciar la API

Para iniciar el servidor local de la API:

```bash
uvicorn app:app --reload
```

Esto ejecutará la API en `http://127.0.0.1:8000`, donde podrás acceder a los diferentes endpoints.

### Métodos Disponibles

- **Últimos datos registrados**:
  ```bash
  GET /jobs/last
  ```

- **Registro de los datos scrapeados**:
  ```bash
  GET /jobs/logs
  ```

- **Datos históricos por fecha**:
  ```bash
  GET /jobs/history/{fecha}
  ```
  Ejemplo:
  ```bash
  GET /jobs/history/02-10-2024
  ```

Para desplegar la API en Vercel, puedes utilizar el siguiente endpoint como referencia:
```bash
# URL de ejemplo en Vercel
https://talento-peru-jobs-kibob9qxx-tjhons-projects.vercel.app/
```

## Tareas Pendientes (TODO)

- [x] **Scrapear datos**:
  - [x] Datos generales de las oportunidades laborales.
  - [x] Integrar datos de las instituciones estatales desde [datosabiertos.gob.pe](https://www.datosabiertos.gob.pe/sites/default/files/ds_lista_entidades_4.csv).
  - [x] Recolectar detalles adicionales sobre cada oferta.
  
- [x] **API (FastAPI)**:
  - [x] Documentación completa con OpenAPI.
  - [ ] Desplegar en Vercel para acceso global.
  - [ ] Crear una instancia de base de datos (gratis) para hacer más eficiente las peticiones 

- [ ] **Automatización con GitHub Actions**:
  - [ ] Implementar scraping automatizado.
  - [ ] **Problema de IP**: La página de SERVIR bloquea peticiones desde IPs que no estén ubicadas en Perú. El uso de proxies gratuitos solo tiene éxito en 2 de 32 casos, y en promedio tarda 10 segundos por página. Se está trabajando en un workflow que verifica periódicamente cuando se habilitan peticiones desde otras IPs.

- [ ] **Crear un paquete de Python**:
  - Facilitar el uso del scraper mediante la creación de un paquete instalable con `pip`.

- [ ] **Web App**:
  - Crear una aplicación web para visualizar y gestionar las ofertas laborales scrapeadas.

## Contribuciones

Si deseas contribuir a este proyecto, por favor abre un *issue* o envía un *pull request*. ¡Tu ayuda será bienvenida!

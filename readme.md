Scrapeando las oportunidades laborales de https://app.servir.gob.pe/DifusionOfertasExterno/faces/consultas/ofertas_laborales.xhtml servir

# Uso

```sh
pip install pipenv
pipenv install
# num_region 1-24
# local: 0 - Github Actions
python .\works.py --n_reg={num_region} --local=0
```

# Docker

```sh
docker-compose run airflow-worker airflow users create --role Admin --username admin --email admin --firstname admin --lastname admin --password admin
```

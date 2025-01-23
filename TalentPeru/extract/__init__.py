from .scrapper.job_scrapper import JobScrapper
import pandas as pd, os
from concurrent.futures import ThreadPoolExecutor, as_completed
from ..utils import today 

# lima = "02"
# deps = [str(n).zfill(2) for n in range(1, 2) if n != 15]
deps = [str(n).zfill(2) for n in range(1, 26) if n != 15]


def ejecutar_dep(departamento) -> pd.DataFrame:
    data_dep = JobScrapper(dep=departamento).scrapper_sequential()
    os.makedirs(f'./data/history/{today}', exist_ok=True)
    dep_path = f'./data/history/{today}/{departamento.zfill(2)}.csv'
    if departamento == "15":
        n = len(data_dep)
        dep_path = f'./data/history/{today}/{departamento.zfill(2)}_{n}.csv'

    data_dep.to_csv(dep_path, index=False)

    return data_dep


def extract_jobs_in_parallel(n_workers=10, lima="15", deps=deps) -> pd.DataFrame:
    def ejecutar_lima(right=True):
        try:
            if right:
                data_dep = JobScrapper(dep=lima).scrapper_both_right()
            else:
                data_dep = JobScrapper(dep=lima).scrapper_both_left()
            return data_dep
        except:
            return pd.DataFrame()

    data_dep_list = []  # almacena datafa4rames

    with ThreadPoolExecutor(max_workers=n_workers) as executor:
        # ejecutamos primero lima por que tiene mayor cantidad de paginas
        future_dep = {
            executor.submit(ejecutar_lima, right_side): f"both_sides_{right_side}"
            for right_side in [True, False]
        }
        future_dep.update({executor.submit(ejecutar_dep, dep): dep for dep in deps})

        for future in as_completed(future_dep):
            data_dep_list.append(future.result())

def get_today_data():
    data_df = []
    dir_dep = f'./data/history/{today}'

    for csv in os.listdir(dir_dep):
        if csv.endswith('.csv'):
            abs_path = os.path.join(dir_dep, csv)
            try:
                df = pd.read_csv(abs_path)
                data_df.append(df)
            except:
                pass
    all_data = pd.concat(data_df, ignore_index=True)
    return all_data
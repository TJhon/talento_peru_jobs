from .scrapper.job_scrapper import JobScrapper
import pandas as pd
from concurrent.futures import ThreadPoolExecutor, as_completed


# lima = "02"
# deps = [str(n).zfill(2) for n in range(1, 3) if n != 15]
deps = [str(n).zfill(2) for n in range(1, 26) if n != 15]


def ejecutar_dep(departamento) -> pd.DataFrame:
    data_dep = JobScrapper(dep=departamento).scrapper_sequential()
    return data_dep


def extract_jobs_in_parallel(n_workers=10, lima="15", deps=deps) -> pd.DataFrame:
    def ejecutar_lima(right=True):
        if right:
            data_dep = JobScrapper(dep=lima).scrapper_both_right()
        else:
            data_dep = JobScrapper(dep=lima).scrapper_both_left()
        return data_dep

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

    data = pd.concat(data_dep_list, ignore_index=True)
    return data

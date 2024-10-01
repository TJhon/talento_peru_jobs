from TalentPeru.Scrapper.with_requests import first_session, left_to_rigth
from time import time
from concurrent.futures import ProcessPoolExecutor
import pandas as pd

deps = [str(n).zfill(2) for n in range(1, 26)]


if __name__ == "__main__":
    start = time()
    session, first_page_soup, view_state_value = first_session()

    def ejecutar(dep):
        data_dep = left_to_rigth(
            dep=dep, view_state_value=view_state_value, session=session
        )
        return data_dep

    data_dep_list = []
    with ProcessPoolExecutor() as executor:
        resultados = list(executor.map(ejecutar, deps[:4]))
        print(resultados)
    # for dep in deps[:4]:

    #     data_dep_list.append(data_dep)
    # print(pd.concat(data_dep_list, ignore_index=True))

    end = time() - start
    print(f"Tiempo de ejecución: {end} segundos")
